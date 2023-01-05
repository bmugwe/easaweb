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
    airfreight_prepaid = ""
    airfreight_postpaid = ""
    others_prepaid = ""
    others_postpaid = ""
    if array["airfreight_charges"] == 1:
        airfreight_postpaid = "Y"
    elif array["other_charges"] == 0:
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

    pdf.cell(
        60,
        4,
        f"[ {airfreight_prepaid} ] PREPAID       [ {airfreight_postpaid} ] COLLECT",
        align="C",
        border=1,
    )
    pdf.cell(
        60,
        4,
        f"[ {others_prepaid} ] PREPAID       [ {others_postpaid} ] COLLECT",
        align="C",
        border=1,
    )
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
    pdf.multi_cell(
        90,
        10,
        f"""
                DATE: {array['timestamp_created']}
                SIGNATURE: .....Boniface.....
                """,
        border=1,
    )

    pdf.output(f"{filename}.pdf", "F")


# Function to create the Airway bill itself


def CreateAirwaybill(array, filename):
    # pdf.set_margins(0, 0, 0)
    print(array)

    p_total_charges = int(array['p_airfreight_charges']) +int(array['p_tax']) + int(array['p_other_charges_agent']) +int(array['p_other_charges_carrier']) +int(array['p_valuation_charges'])
    c_total_charges = 1 +int(array['c_tax']) + int(array['c_other_charges_agent']) +int(array['c_other_charges_carrier']) +int(array['c_valuation_charges'])
    
    # if array['airfreight_charges'] == 1:
    #     airfreight_postpaid = "Y"
    # elif array['other_charges'] == 0:
    #     others_prepaid = "Y"
    # else:
    #     airfreight_postpaid = "Y"
    #     others_postpaid = "Y"
    pdf.set_font("Arial", "B", 10)

    pdf.cell(180, 3, f"Airway Bill", align="c")
    pdf.set_font("Arial", "B", 6)
    pdf.cell(180, 2, "", ln=1)
    # Save top coordinate
    top = pdf.y + 3

    # Calculate x position of next cell
    offset = pdf.x + 90
    pdf.cell(90, 3, ln=1)
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
    pdf.set_font("Arial", "B", 5)
    pdf.multi_cell(
        90,
        5,
        f"""Not negotiable:  
            Air Waybill: (Air Consignment note) 

            issued by 
            _______________________________________________________________________________
            Copies 1,2 and 3 of the Air Waybill are originals and have the same validity
            it is agreed that the goods described herein are accepted in apparent good 
            order and condition (except as noted) for carriage SUBJECT TO THE
            CONDITIONS OF CONTRACT ON THE REVERSE HEREOF. ALL GOODS MAY 
            BE CARRIED BY ANY OTHER MEANS INCLUDING ROAD OR ANY OTHER
            CARRIER UNLESS SPECIFIC CONTRARY INSTRUCTIONS ARE GIVEN HEREON 
            BY THE SHIPPER, AND SHIPPERS AGREES THAT THE SHIPMENT MAY BE 
            CARRIED VIA INTERMEDIATE STOPPING PLACES WHICH THE CARRIER 
            DEEMS APPROPRIATE. THE SHIPPER'S ATTENTION IS DRAWN TO THE 
            NOTICE CONCERNING CARRIER'S LIMITATION OF LIABILITY. Shipper 
            may increase such limitation of liability bydeclaring a higher value for 
            carriage and paying a supplemental charge if required.""",
        border=1,
        align="l",
    )

    pdf.cell(0, 1, "", ln=1)
    pdf.y = top + 24
    pdf.set_font("Arial", "B", 5)
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

    pdf.cell(90, 4, f"Issuing Carrier's Agent Name and City", border=1, ln=1)
    pdf.cell(
        90,
        4,
        f"{array['IATA_NAME']} {array['IATA_CITY']}",
        border=1,
        ln=1,
    )

    pdf.cell(45, 4, f"Agent's IATA Code: {array['IATA_CODE']}", border=1)
    pdf.cell(45, 4, f"Account No.: {array['IATA_ACCNO']}", border=1, ln=1)

    pdf.cell(
        90,
        4,
        f"Airport of Destination: {array['AIRPORT_OF_DEST']}",
        border=1,
        ln=1,
    )
    pdf.cell(
        90,
        4,
        f" - ",
        border=1,
        ln=1,
    )

    pdf.cell(90, 4, f"Accounting Information: ", border=1, ln=1)
    pdf.cell(90, 4, f"Reference Number: ", border=1, ln=1)

    pdf.cell(
        90,
        6,
        f"Airport of Departure (addr. of First Carrier and requested Routing",
        border=1,
        ln=1,
    )
    pdf.cell(90, 6, f"{array['Airport_of_departure']}  {array['Requested_routing']}", border=1, ln=1)
    pdf.set_font("Arial", "B", 5)
    pdf.cell(0, 2, "", ln=1)
    # pdf.cell(0, 10, "", border=2)
    # START HEADERS
    pdf.cell(45, 3, f"First Carrier", border=1)
    pdf.cell(45, 3, f"Routing Information", border=1)
    pdf.cell(45, 3, f"Airport of Destination", border=1)
    pdf.cell(45, 3, f"Flight Date", border=1, ln=1)

    # END OF HEADERS
    # pdf.cell(0, 2, "", )
    # START BODY
    pdf.cell(45, 10, f"{array['FIRST_CARRIER']}", border=0)
    pdf.cell(45, 10, f"{array['Requested_routing']} {array['ROUTING_DEST']}", border=0)
    pdf.cell(45, 10, f"{array['AIRPORT_OF_DEST']}", border=0)
    pdf.cell(45, 10, f"{array['flight_date']}", border=0, ln=1)

    # END OF BODY
   
    # START HEADERS
    pdf.cell(20, 3, f"", border=1, align="c")
    pdf.cell(20, 3, f"Gross weight ", border=1, align="c")
    pdf.cell(30, 3, f"Rate class Commodity", border=1, align="c")
    pdf.cell(30, 3, f"Chargeable", border=1, align="c")
    pdf.cell(30, 3, f"", border=1, align="c")
    pdf.cell(20, 3, f"", border=1, align="c")
    pdf.cell(40, 3, f"Nature & Quantity", ln=1, border=1, align="c")
    # START HEADERS 2
    pdf.cell(20, 3, f"NO.", border=1, align="c")
    pdf.cell(20, 3, f"Gross weight ", border=1, align="c")
    pdf.cell(30, 3, f"Item No.", border=1, align="c")
    pdf.cell(30, 3, f"Weight", border=1, align="c")
    pdf.cell(30, 3, f"Rate Charge", border=1, align="c")
    pdf.cell(20, 3, f"Total", border=1, align="c")
    pdf.cell(40, 3, f"of Goods", ln=1, border=1, align="c")

    # END OF HEADERS
    # pdf.cell(0, 2, "", , border=1)
    # START BODY
    pdf.cell(20, 30, f"1. ", border=1)
    pdf.cell(20, 30, f"{array['weight']}", border=1)
    pdf.cell(30, 30, f"{array['commodity_item_no']}", border=1)
    pdf.cell(30, 30, f"{array['cheargeable_weight']}", border=1)
    pdf.cell(30, 30, f"{array['Rate_charge']}", align="C", border=1)
    pdf.cell(20, 30, f"{array['total_charge']}", align="C", border=1)
    pdf.cell(40, 30, f"{array['description']} Kgs", align="C", ln=1, border=1)

    # END OF BODY
    pdf.cell(0, 10, "", ln=1)
    # pdf.cell(180, 1, "", border=1, ln=1)
    pdf.cell(30, 4, f"Prepaid", border=1, align="c")
    pdf.cell(20, 4, f"Weight Charge", border=1, align="c")
    pdf.cell(30, 4, f"Postpaid", border=1, align="c")
    pdf.multi_cell(100, 25, f"Other Charges", border=1, ln=1)

    pdf.y = top+145
    pdf.cell(40, 4, f"{array['p_airfreight_charges']}", border=1)
    pdf.cell(40, 4, f"{array['c_airfreight_charges']}", border=1, ln=1)

    pdf.cell(30, 4, f"", border=1)
    pdf.cell(20, 4, f"Valuation Charge", border=1, align="c")
    pdf.cell(30, 4, f"", border=1, ln=1)

    pdf.cell(40, 4, f"{array['p_valuation_charges']}", border=1)
    pdf.cell(40, 4, f"{array['c_valuation_charges']}", border=1, ln=1)

    pdf.cell(30, 4, f"", border=1)
    pdf.cell(20, 4, f"Tax", border=1, align="c")
    pdf.cell(30, 4, f"", border=1,ln=1)

    pdf.cell(40, 4, f"{array['p_tax']}", border=1)
    pdf.cell(40, 4, f"{array['c_tax']}", border=1, ln=1)

    pdf.cell(20, 4, f"", border=1)
    pdf.cell(40, 4, f"Total Other Charges due to agent", border=1, align="c")
    pdf.cell(20, 4, f"", border=1, ln=1)

    pdf.cell(40, 4, f"{array['p_other_charges_agent']}", border=1)
    pdf.cell(40, 4, f"{array['c_other_charges_agent']}", border=1, ln=1)

    pdf.cell(20, 4, f"", border=1)
    pdf.cell(40, 4, f"Total Other Charges due to Carrier", border=1, align="c")
    pdf.cell(20, 4, f"", border=1)
    pdf.multi_cell(100, 2, f"""
                            Shippers certifies that the particulars on the face hereof are correct and that insofar any part
                             of the consignment contains dangerous goods, such part is properly described by name and is in 
                             proper consition for carrieage accordingly to the applicable Dangerous goods Regulation
                            ____________________________________________________________________________________________
                            Signature of Shipper or his agent
                            """, border=1, ln=1, align="l")

    pdf.y = top+177
    pdf.cell(40, 4, f"{array['p_other_charges_carrier']}", border=1)
    pdf.cell(40, 4, f"{array['c_other_charges_carrier']}", border=1, ln=1)

    pdf.cell(40, 4, f"", border=1)
    pdf.cell(40, 4, f"", border=1, ln=1)

    pdf.cell(80, 5, border=1, ln=2)

    pdf.cell(40, 4, f"Total Prepaid",  border=1, align="c")
    pdf.cell(40, 4, f"Total collect", border=1, align="c")
    pdf.multi_cell(100, 2, f"""
                            
                            ---------------------------------------------------------------------------------
                            Executed on (date)                at (place)                        Signature of issuing Carrier or its agent
                             """, border=1, ln=1, align="c")

    pdf.y = top+195
    pdf.cell(40, 4, f"{p_total_charges}",  border=1,)
    pdf.cell(40, 4, f"{c_total_charges}", border=1, ln=1)

    pdf.cell(80, 5, border=1, ln=2)

    pdf.cell(40, 4, f"Currency Conversion Rates",  border=1, align="c")
    pdf.cell(40, 4, f"CC Charges in Dest. Currency", border=1, ln=1, align="c")

    pdf.cell(40, 4, f"{125}",  border=1,)
    pdf.cell(40, 4, f"{124}", border=1, ln=1)

    pdf.cell(80, 4, f"For Carrier's Use Only at Destination",  border=1, ln=1, align="c")

    pdf.cell(40, 4, f"Charges at Destination",  border=1, align="c")
    pdf.cell(40, 4, f"Total Collect Charges", border=1, ln=1, align="c")

    pdf.cell(40, 4, f"{array['p_total_charges']}",  border=1,)
    pdf.cell(40, 4, f"{array['c_total_charges']}", border=1, ln=1)



    pdf.set_font("Arial", "B", 6)

    

    pdf.output(f"{filename}.pdf", "F")
