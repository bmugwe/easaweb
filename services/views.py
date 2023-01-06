from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . import functions as fsa

# from functions import CreateAirwaybill, CreateInvoice

from .forms import Invoicetemplate, Airwaybill, COUNTRIES
from .models import InvoiceLetter , airwaybill

# Create your views here.
@login_required
def servicesInv(request):
    now = timezone.now()
    current_user = request.user
    user_instance = User.objects.get(username=current_user)
    if request.method == "POST":
        sent_data = request.POST
        print(sent_data)
        try:
            InvoiceLetter(
                from_companyname=sent_data.get("from_companyname"),
                from_personname=sent_data.get("from_personname"),
                from_address=sent_data.get("from_address"),
                from_phonenumber=sent_data.get("from_phonenumber"),
                from_sendertown=sent_data.get("from_town"),
                from_emailaddress=sent_data.get("from_emailaddress"),
                to_consigneeename=sent_data.get("to_consigneeename"),
                to_phonenumber=sent_data.get("to_phonenumber"),
                to_address=sent_data.get("to_address"),
                to_receivertown=sent_data.get("to_town"),
                # from_personname = sent_data.get('from_personname'),
                from_countries=sent_data.get("from_countries"),
                from_town=sent_data.get("from_town"),
                to_countries=sent_data.get("to_countries"),
                to_town=sent_data.get("to_town"),
                package_kind=sent_data.get("package_kind"),
                quantity=sent_data.get("quantity"),
                description=sent_data.get("description"),
                weight=sent_data.get("weight"),
                length=sent_data.get("length"),
                width=sent_data.get("width"),
                height=sent_data.get("height"),
                airfreight_charges=sent_data.get("airfreight_charges"),
                other_charges=sent_data.get("other_charges"),
                insur_amount=sent_data.get("insur_amount"),
                nvd=sent_data.get("nvd"),
                ncv=sent_data.get("ncv"),
                handling_info=sent_data.get("handling_info"),
                user_saved_by=user_instance,
            ).save()
        except Exception as e:
            print(f"Error saving the data:  {e}")

        messages.success(request, "The invoice Letter has been added successfully")
        return redirect("services-invoice")
    else:
        data = {}

        form = Invoicetemplate(data=data)
        context = {"form": form, "data": data}

        return render(request, "services/invoice.html", context)


@login_required
def servicesAirway(request, id):
    inv_id_f = InvoiceLetter.objects.filter(inv_id=id)
    current_user = request.user
    user_instance = User.objects.get(username=current_user)
    if request.method == "POST":
        sent_data = request.POST
        inv_id_fo = InvoiceLetter.objects.get(inv_id=id)
        if((sent_data.get('accept')) == 'on'):
            accept_status = True
        else:
            accept_status = False
        try:
            airwaybill(
                inv_id=inv_id_fo,
                from_companyname=sent_data.get("from_companyname"),
                from_personname=sent_data.get("from_personname"),
                from_address=sent_data.get("from_address"),
                from_phonenumber=sent_data.get("from_phonenumber"),
                from_sendertown=sent_data.get("from_town"),
                from_emailaddress=sent_data.get("from_emailaddress"),
                to_consigneeename=sent_data.get("to_consigneeename"),
                to_phonenumber=sent_data.get("to_phonenumber"),
                to_address=sent_data.get("to_address"),
                to_receivertown=sent_data.get("to_town"),
                # from_personname = sent_data.get('from_personname'),
                from_countries=sent_data.get("from_countries"),
                from_town=sent_data.get("from_town"),
                to_countries=sent_data.get("to_countries"),
                to_town=sent_data.get("to_town"),
                package_kind=sent_data.get("package_kind"),
                quantity=sent_data.get("quantity"),
                description=sent_data.get("description"),
                weight=sent_data.get("weight"),
                length=sent_data.get("length"),
                width=sent_data.get("width"),
                height=sent_data.get("height"),
                airfreight_charges=sent_data.get("airfreight_charges"),
                other_charges=sent_data.get("other_charges"),
                insur_amount=sent_data.get("insur_amount"),
                nvd=sent_data.get("nvd"),
                ncv=sent_data.get("ncv"),
                handling_info=sent_data.get("handling_info"),
                user_saved_by_id=user_instance.id,
                Airport_of_departure = sent_data.get('Airport_of_departure'),
                AIRPORT_OF_DEST = sent_data.get('AIRPORT_OF_DEST'),
                Airport_of_destination = sent_data.get('Airport_of_destination'),
                c_airfreight_charges = sent_data.get('c_airfreight_charges'),
                c_charges_dest = sent_data.get('c_charges_dest'),
                c_other_charges_agent = sent_data.get('c_other_charges_agent'),
                c_other_charges_carrier = sent_data.get('c_other_charges_carrier'),
                c_tax = sent_data.get('c_tax'),
                c_total_charges = sent_data.get('c_total_charges'),
                c_valuation_charges = sent_data.get('c_valuation_charges'),
                Carrier_name = sent_data.get('Carrier_name'),
                cheargeable_weight = sent_data.get('cheargeable_weight'),
                commodity_item_no = sent_data.get('commodity_item_no'),
                FIRST_CARRIER = sent_data.get('FIRST_CARRIER'),
                IATA_ACCNO = sent_data.get('IATA_ACCNO'),
                IATA_CITY = sent_data.get('IATA_CITY'),
                IATA_CODE = sent_data.get('IATA_CODE'),
                IATA_NAME = sent_data.get('IATA_NAME'),
                other_charges_2 = sent_data.get('other_charges_2'),
                p_airfreight_charges = sent_data.get('p_airfreight_charges'),
                p_charges_dest = sent_data.get('p_charges_dest'),
                p_currency_conversion = sent_data.get('p_currency_conversion'),
                p_other_charges_agent = sent_data.get('p_other_charges_agent'),
                p_other_charges_carrier = sent_data.get('p_other_charges_carrier'),
                p_tax = sent_data.get('p_tax'),
                p_total_charges = sent_data.get('p_total_charges'),
                p_valuation_charges = sent_data.get('p_valuation_charges'),
                Rate_charge = sent_data.get('Rate_charge'),
                Requested_routing = sent_data.get('Requested_routing'),
                ROUTING_DEST = sent_data.get('ROUTING_DEST'),
                total_charge = sent_data.get('total_charge'),
                flight_date = sent_data.get('flight_date'),
                accept = accept_status,
            ).save()

            invoice_p = InvoiceLetter.objects.get(inv_id=id)
            invoice_p.is_processed = True
            invoice_p.save()

            messages.success(request, "The Airway bill has been added successfully")

        except Exception as e:
            print(f"Error saving the data:  {e}")
            messages.error(request, f"The Airway bill did not save {e}")

        return redirect("dashboard-products")
    else:
        invoicedatas = inv_id_f.values()
        data = {}
        for invoice in invoicedatas:
            for inv in invoice:
                data[inv] = invoice.get(inv)

        for i in COUNTRIES:
            if i[0]==data.get('from_countries'):
                data['from_countries1'] = i[1]
            if i[0]==data.get('to_countries'):
                data['to_countries1'] = i[1]
        print(data)
        form = Airwaybill(data=data)

        context = {
            "form": form,
            "data": data
        }

        return render(request, "services/airwaybill.html", context)


def print_invoice(request, id):
    invoiceDetails = InvoiceLetter.objects.filter(inv_id=id).values()[0]
    # breakpoint()
    fromCompany = invoiceDetails["from_companyname"]
    fromPerson = invoiceDetails["from_personname"]

    filename = f"{fromCompany} - {fromPerson}"
    data = {}
    inv_id_f = InvoiceLetter.objects.filter(inv_id=id)
    invoicedatas = inv_id_f.values()
    for invoice in invoicedatas:
        for inv in invoice:
            data[inv] = invoice.get(inv)

    fsa.CreateInvoice(data, filename=filename)
    return FileResponse(
        open("" + filename + ".pdf", "rb"),
        as_attachment=True,
        content_type="application/pdf",
    )


def generateAirwaybill(request, id):

    invoiceDetails = InvoiceLetter.objects.filter(inv_id=id).values()[0]

    fromCompany = invoiceDetails["from_companyname"]
    fromPerson = invoiceDetails["from_personname"]

    filename = f"{fromCompany} - {fromPerson}"
    data = {}

    inv_id_f = airwaybill.objects.filter(inv_id=id)
    invoicedatas = inv_id_f.values()
    for invoice in invoicedatas:
        for inv in invoice:
            data[inv] = invoice.get(inv)


    sales = [
        {"item": "Keyboard", "amount": "$120,00"},
        {"item": "Mouse", "amount": "$10,00"},
        {"item": "House", "amount": "$1 000 000,00"},
    ]
    # data["sales"] = sales
    print(data)

    # pdf.output('report.pdf', 'F')
    fsa.CreateAirwaybill(data, filename=filename)
    return FileResponse(
        open("" + filename + ".pdf", "rb"),
        as_attachment=True,
        content_type="application/pdf",
    )
