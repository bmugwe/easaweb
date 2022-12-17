from datetime import datetime, timedelta
from django.db import connection
from django.core.cache import cache

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()


# Function to create the Airway bill  Invoice
def CreateInvoice(array, filename):
    # pdf.set_margins(0, 0, 0)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(90, 6, f"Shipper's Name and Address {array['name']}")
    pdf.cell(90, 6, "Company heading", ln=1)
    pdf.set_font("Arial", "B", 6)
    pdf.cell(0, 2, "", ln=1)

    pdf.multi_cell(180, 6, "Shipper's \n ...... \n .......... \n ......... ", border=1,align='R')
    # pdf.cell(90, 6, "Company heading")
    pdf.cell(50, 16, "Consignee", border=1)
    pdf.cell(
        90,
        16,
        "You are hereby requested and authorised upon receipt of ........",
        ln=1,
        border=1,
    )

    pdf.cell(90, 16, "")
    pdf.cell(
        90, 16, "I certify thata the contents of this consignment.....", ln=1, border=1
    )

    pdf.cell(45, 16, "Airport of Departure.", border=1)
    pdf.cell(45, 16, "Airport of Destination.", border=1)
    pdf.cell(90, 16, "", ln=1)
    pdf.cell(90, 16, "REQUESTED ROUTING", border=1, ln=1)
    pdf.cell(90, 16, "REQUESTED BOOKING", border=1, ln=1)
    pdf.cell(180, 1, "", border=1, ln=1)
    pdf.cell(
        180,
        16,
        "MARKS AND NUMBERS:                                      NO. & KIND OF PKGS:                                  DESC OF GOODS:                                     GROSS WEIGHT MEASUREMENTS:",
        border=1,
        ln=1,
    )
    pdf.cell(180, 50, "", border=1, ln=1)
    pdf.cell(180, 1, "", border=1, ln=1)

    pdf.set_font("Arial", "B", 6)

    pdf.multi_cell(
        180,
        4,
        "AIR FREIGHT CHARGES (MARK ONE TO APPLY):       OTHER CHARGES AT ORIGIN (MARK ON TO APPLY):                                INSURANCE - AMMOUNT REQUESTED:",
    )
    pdf.set_font("Arial", "B", 5)
    pdf.cell(0, 2, "", ln=1)

    pdf.cell(60, 4, "[  ] PREPAID       [  ] COLLECT", align="C")
    pdf.cell(60, 4, "[  ] PREPAID       [  ] COLLECT", align="C")
    pdf.cell(60, 4, "xxxx", align="C", ln=1)
    pdf.cell(0, 2, "", ln=1)
    pdf.set_font("Arial", "B", 8)

    pdf.cell(90, 4, "DECLARED CALUE", align="C", border=1)
    pdf.cell(90, 4, "", align="C", ln=1)

    pdf.set_font("Arial", "B", 6)
    pdf.cell(45, 14, "FOR CARRIAGE (NVD )", align="C", border=1)
    pdf.cell(45, 14, "FOR CUSTOMS (NCV)", align="C", border=1)
    pdf.cell(90, 14, "", align="C", ln=1)

    pdf.set_font("Arial", "B", 6)
    pdf.cell(90, 24, "HANDLING INFORMATION AND REMARKS", border=1)
    pdf.multi_cell(90, 14, "DATE    \nSIGNATURE........")

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
