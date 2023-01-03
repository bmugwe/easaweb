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
    # pdf.set_margins(0, 0, 0)
    print(array)
    airfreight_prepaid  = ""
    airfreight_postpaid = ""
    others_prepaid = ""
    others_postpaid = ""
    # if array['airfreight_charges'] == 1:
    #     airfreight_postpaid = "Y"
    # elif array['other_charges'] == 0:
    #     others_prepaid = "Y"
    # else:
    #     airfreight_postpaid = "Y"
    #     others_postpaid = "Y"
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
