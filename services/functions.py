from datetime import datetime, timedelta
from django.db import connection
from django.core.cache import cache

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()


COUNTRIES = {
    "0": "Select Country",
    "1": "Burundi",
    "2": "Democratic Republic of Congo",
    "3": "Kenya",
    "4": "Rwanda",
    "5": "South Sudan",
    "6": "Tanzania",
    "7": "Uganda",
}

KIND_OF_PACKAGE = {
    "0": "Select Package Kind",
    "1": "Cardboard/Fiberboard",
    "2": "Bagged Cargo",
    "3": "Wooden Cases",
    "4": "Wooden Crates",
    "5": "Steel Drums",
    "6": "Bales",
    "7": "Palletizing Cargo",
    "8": "Containers",
}


# Function to create the Airway bill  Invoice
def CreateInvoice(array, filename):
    # pdf.set_margins(0, 0, 0)
    airfreight_prepaid  = ""
    airfreight_postpaid = ""
    others_prepaid = ""
    others_postpaid = ""
    if array['airfreight_charges'] == 1:
        airfreight_postpaid = "Y"
    elif array['other_charges'] == 0:
        others_prepaid = "Y"
    else:
        airfreight_postpaid = "Y"
        others_postpaid = "Y"
    pdf.set_font("Arial", "B", 10)

    pdf.cell(180, 2, f"Shipper's Name and Address ")
    pdf.set_font("Arial", "B", 6)
    pdf.cell(180, 2, "", ln=1)
    # Save top coordinate
    top = pdf.y

    # Calculate x position of next cell
    offset = pdf.x + 90

    pdf.multi_cell(
        90,
        4,
        f"""Shipper's:  
            Name: {array['from_personname']},
            P.O. Box : {array['from_address']},
            City: {array['from_sendertown']},
            Contact: {array['from_emailaddress']} - {array['from_phonenumber']},
        """,
        border=1,
        align="L",
    )
    # Reset y coordinate
    pdf.y = top

    # Move to computed offset
    pdf.x = offset

    pdf.multi_cell(
        90,
        5,
        f""" 
            Company Header: 
            Company Header: 
            Company Header: 
            You are hereby requested and authorised upon receipt of 
            the consignment described herein to prepare and sign the 
            Air Waybill and other necessary documents on our 
            behalf and dispatch the consignment in accordance with your
            Condition of Contract.           
            I certify that the contents of this consignment are 
            properly identified by name. Insofar as any part of the 
            consigment contains dangerous goods, such part is in 
            proper condition for carriage by air according to the 
            applicable Dangerous Goods Regulations.
        """,
        border=1,
        align="c",
    )
    pdf.cell(0, 1, "", ln=1)
    pdf.y = top + 24

    pdf.multi_cell(
        90,
        4,
        f"""Consignee: 
            Name: {array['to_consigneeename']},
            P.O. Box : {array['to_address']},
            City: {array['to_receivertown']},
        """,
        border=1,
        align="L",
    )
    pdf.cell(0, 1, "", ln=1)

    pdf.cell(
        45, 10, f"Airport of Departure: {COUNTRIES[array['from_countries']]}", border=1
    )
    pdf.cell(
        45, 10, f"Airport of Destination: {COUNTRIES[array['to_countries']]}", border=1
    )
    pdf.cell(90, 10, "", ln=1)
    pdf.cell(90, 10, "REQUESTED ROUTING", border=1, ln=1)
    pdf.cell(90, 10, "REQUESTED BOOKING", border=1, ln=1)

    pdf.set_font("Arial", "B", 6)
    pdf.cell(0, 2, "", ln=1)
    # pdf.cell(0, 10, "", border=2)
    # START HEADERS
    pdf.cell(30, 3, f"MARKS & NUMBERS", border=1)
    pdf.cell(10, 3, f"NO: ", border=1)
    pdf.cell(36, 3, f"KIND OF PACKAGES", border=1)
    pdf.cell(60, 3, f"DESCRIPTION OF GOODS", border=1)
    pdf.cell(25, 3, f"GROSS WEIGHT", border=1)
    pdf.cell(25, 3, f"MEASUREMENT", border=1, ln=1)

    # END OF HEADERS
    # pdf.cell(0, 2, "", )
    # START BODY
    pdf.cell(30, 10, f"1. ", border=0)
    pdf.cell(10, 10, f"{array['quantity']}", border=0)
    pdf.cell(36, 10, f"{KIND_OF_PACKAGE[array['package_kind']]}", border=0)
    pdf.cell(60, 10, f"{array['description']}", border=0)
    pdf.cell(25, 10, f"{array['weight']} Kgs", border=0, align="C")
    pdf.cell(
        25,
        10,
        f"{array['length']} * {array['width']} * {array['height']} cm",
        ln=1,
        align="C",
    )

    # END OF BODY
    pdf.cell(0, 30, "", ln=1)
    # pdf.cell(180, 1, "", border=1, ln=1)

    pdf.set_font("Arial", "B", 6)

    # pdf.multi_cell(
    #     180,
    #     4,
    #     f"                                       ",
    #     border=1
    pdf.cell(60, 4, f"AIR FREIGHT CHARGES (MARK ONE TO APPLY):", align="C", border=1)
    pdf.cell(60, 4, f"OTHER CHARGES AT ORIGIN (MARK ON TO APPLY):", align="C", border=1)
    pdf.cell(60, 4, f"INSURANCE - AMMOUNT REQUESTED: ", align="C", ln=1, border=1)

    pdf.cell(60, 4, f"[ {airfreight_prepaid} ] PREPAID       [ {airfreight_postpaid} ] COLLECT", align="C", border=1)
    pdf.cell(60, 4, f"[ {others_prepaid} ] PREPAID       [ {others_postpaid} ] COLLECT", align="C", border=1)
    pdf.cell(60, 4, f"KES {array['insur_amount']} ", align="C", ln=1, border=1)
    pdf.cell(0, 2, "", ln=1)
    pdf.set_font("Arial", "B", 8)

    pdf.cell(90, 4, "DECLARED VALUE", align="C", border=1)
    pdf.cell(90, 4, "", align="C", ln=1)

    pdf.set_font("Arial", "B", 6)
    pdf.cell(45, 7, "FOR CARRIAGE (NVD)", align="C", border=1)
    pdf.cell(45, 7, "FOR CUSTOMS (NCV)", align="C", border=1, ln=1)
    pdf.cell(45, 7, f"{array['nvd']}", align="C", border=1)
    pdf.cell(45, 7, f"{array['ncv']}", align="C", border=2)
    pdf.cell(90, 14, "", align="C", ln=1)

    pdf.set_font("Arial", "B", 6)
    pdf.cell(90, 4, "HANDLING INFORMATION AND REMARKS", border=1)
    pdf.cell(90, 4, "", border=1, ln=1)
    pdf.cell(90, 40, f"{array['handling_info']}", border=1)
    pdf.multi_cell(90, 10, 
                f"""
                DATE: {array['timestamp_created']}
                SIGNATURE: .....Boniface.....
                """, 
                border=1)

    pdf.output(f"{filename}.pdf", "F")


# Function to create the Airway bill itself


def CreateAirwaybill(array, filename):
    pdf.set_font("Arial", "B", 6)
    pdf.cell(50, 6, "Shipper's Name and Address: .......................... ", border=1)
    pdf.cell(50, 6, "Shipper's Account Number: ............................", border=1)
    pdf.multi_cell(
        80,
        8,
        "Not negotiable:............... \nAir Waybill(Air Consignment note.) \nissued by: ...................",
        border=1,
    )
    pdf.cell(
        50,
        6,
        "",
    )
    pdf.cell(
        50,
        6,
        "",
    )
    pdf.multi_cell(
        80,
        8,
        "Copies 1,2 and 3 ot this Air Waybul are original and have the same Validity.",
        border=1,
    )
    pdf.cell(50, 6, "Consignee's Name and Address", border=1)
    pdf.cell(50, 6, "consignee;s Account Number", border=1)
    pdf.multi_cell(
        80,
        8,
        "It is agreed  tha the goods described herin are accepted ub aooarebt good order and condition (exept)...",
        border=1,
    )

    pdf.cell(100, 6, "Issueing  Carriers Agent Name and city: .........", border=1)
    pdf.cell(80, 6, "Accounting Information: .........", border=1, ln=1)
    # pdf.cell(20, 10, 'Title', 1, 1, 'C');
    # pdf.cell(50, 6, "",)
    pdf.cell(50, 6, "Agents IATA No: .......................... ", border=1)
    pdf.cell(50, 6, "Account no: ............................", border=1)
    pdf.cell(80, 6, "", ln=1)
    pdf.cell(
        100,
        12,
        "Airport of Departure (Addr. of First Carrier) and Requested Routing:",
        border=1,
    )
    pdf.cell(
        80,
        12,
        "Refference Number:.................    Optional Shipping information:.....................",
        border=1,
        ln=1,
    )
    pdf.cell(
        10,
        24,
        "To: ..... ",
        border=1,
    )
    pdf.cell(40, 24, "By First Carrier:.................", border=1)
    pdf.cell(10, 24, "To:...... ", border=1)
    pdf.cell(10, 24, "By:...... ", border=1)
    pdf.cell(10, 24, "To:...... ", border=1)
    pdf.cell(10, 24, "By:...... ", border=1)
    pdf.cell(20, 24, "Currency:.. ", border=1)
    pdf.cell(20, 24, "CHGS Code:.. ", border=1)
    pdf.multi_cell(
        50,
        8,
        "WT/val:... Other:...   PDD:  COLL:  PDD:  COLL:  \n Declared Value for carriage:\nDeclared Values for customs:  ",
        border=1,
    )
    # pdf.cell(90, 16, "", border=1)
    pdf.cell(50, 16, "Airport of Destination: .... ", border=1)
    pdf.cell(20, 16, "Fight/Date: .........", border=1)
    pdf.cell(22, 3, "for Carrier Use Only", border=1)
    pdf.cell(22, 16, "Fight/Date: ...", border=1)
    pdf.cell(32, 16, "Ammount of insurance:", border=1)
    pdf.cell(34, 16, "Insurance: if carrier offers...", border=1, ln=1)
    pdf.multi_cell(
        180,
        16,
        "Handling Information: ......... \n (For U.S.A use only) These commodities... ",
        border=1,
    )
    pdf.cell(20, 26, "No of Pieces RCP", border=1)
    pdf.cell(20, 26, "Gross Weight", border=1)
    pdf.cell(8, 26, "Kg/lb", border=1)
    pdf.cell(25, 26, "Commodity Item No.", border=1)
    pdf.cell(25, 26, "Chargeable weight.", border=1)
    pdf.cell(25, 26, "Rates Charge:", border=1)
    pdf.cell(25, 26, "Total ", border=1)
    pdf.multi_cell(32, 26, "Nature and Quality of Goods ", border=1)

    pdf.cell(20, 16, "", border=1)
    pdf.cell(20, 16, "", border=1)
    pdf.cell(8, 16, "", border=1)
    pdf.cell(25, 16, "", border=1)
    pdf.cell(25, 16, "", border=1)
    pdf.cell(25, 16, "", border=1)
    pdf.cell(25, 16, " ", border=1)
    pdf.cell(32, 16, "", border=1, ln=1)

    pdf.cell(20, 16, "Prepaid", border=1)
    pdf.cell(20, 16, "Weight Charge", border=1)
    pdf.cell(20, 16, "Collect", border=1)
    pdf.cell(120, 16, "Other Charges:", border=1, ln=1)

    pdf.cell(
        180,
        6,
        "Valuation Charge:................... \nTax:...................  \nWeight Charge:.................. \nTotal_Other_Charges Due agent:.................. \nTotal Prepaid:............................. ",
        ln=1,
    )
    pdf.cell(
        180,
        6,
        "Total Collect:............................. Currency Convertion Rates:................ CC Chargres in Dest. Currency:................  ",
        ln=1,
    )
    pdf.cell(
        180,
        6,
        "For Carrier's Use Only at destination:.............. Chargess at destination:.........",
        ln=1,
    )

    pdf.multi_cell(
        180,
        6,
        "Shippers certifies that the particulars on the face hereof are correct and that insofar as any ....... \n ..................................................... \n Signature of Shipper or his Agent. \n ........................ \n Executred on(date)    at(place)  Signature of issuingCarrirs or its Agents.",
        border=1,
        align="C",
    )
    # pdf.cell(60, 4, "", border=1)
    # pdf.cell(10, 6, "Other", border=1, )
    # pdf.cell(10, 6, "ppd", border=1)
    # pdf.cell(20, 6, "Routing and Destination: ................... ", border=1)
    # pdf.multi_cell(100, 12, "Not negotiable \n Air Waybill", border=1)
    # pdf.cell(190, 265, border = 1)
    pdf.output(f"{filename}.pdf", "F")
