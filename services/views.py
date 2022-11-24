from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from fpdf import FPDF



from .forms import Invoicetemplate, Airwaybill
from .models import InvoiceLetter, airwaybill

# Create your views here.
def servicesInv(request):
    now = timezone.now()
    print(request.method)
    if request.method == 'POST':
        sent_data = request.POST
        print(sent_data)
        try:
            InvoiceLetter(
                from_companyname = sent_data.get('from_companyname'),
                from_personname = sent_data.get('from_personname'),
                from_address = sent_data.get('from_address'),
                from_phonenumber = sent_data.get('from_phonenumber'),
                from_sendertown = sent_data.get('from_town'),
                from_emailaddress = sent_data.get('from_emailaddress'),
                to_consigneeename = sent_data.get('to_consigneeename'),
                to_phonenumber = sent_data.get('to_phonenumber'),
                to_address = sent_data.get('to_address'),
                to_receivertown = sent_data.get('to_town'),
                # from_personname = sent_data.get('from_personname'),
                from_countries = sent_data.get('from_countries'),
                from_town = sent_data.get('from_town'),
                to_countries = sent_data.get('to_countries'),
                to_town = sent_data.get('to_town'),
                package_kind = sent_data.get('package_kind'),
                quantity = sent_data.get('quantity'),
                description = sent_data.get('description'),
                weight  = sent_data.get('weight'),
                length = sent_data.get('length'),
                width = sent_data.get('width'),
                height = sent_data.get('height'),
                airfreight_charges = sent_data.get('airfreight_charges'),
                other_charges = sent_data.get('other_charges'),
                insur_amount = sent_data.get('insur_amount'),
                nvd = sent_data.get('nvd'),
                ncv = sent_data.get('ncv'),
                handling_info = sent_data.get('handling_info')
            ).save()
        except Exception as e:
            print(f"Error saving the data:  {e}")
        
        messages.success(request, "The invoice Letter has been addes successfully")
        return redirect('services-invoice')
    else:
        data =  {
            "from_companyname": "Equitexy Business Solutions",
            "from_personname": 'Boniface Mugwe'
        }
        form = Invoicetemplate(data=data)
        context = {
            'form': form,
            'data': data
        }
    
        return render(request, 'services/invoice.html', context)

@login_required
def servicesAirway(request, id):
    inv_id_f = InvoiceLetter.objects.filter(inv_id = id)
    if request.method == 'POST':
        sent_data = request.POST
        inv_id_fo = InvoiceLetter.objects.get(inv_id = id)
        try:
            airwaybill(
                inv_id = inv_id_fo,
                from_companyname = sent_data.get('from_companyname'),
                from_personname = sent_data.get('from_personname'),
                from_address = sent_data.get('from_address'),
                from_phonenumber = sent_data.get('from_phonenumber'),
                from_sendertown = sent_data.get('from_town'),
                from_emailaddress = sent_data.get('from_emailaddress'),
                to_consigneeename = sent_data.get('to_consigneeename'),
                to_phonenumber = sent_data.get('to_phonenumber'),
                to_address = sent_data.get('to_address'),
                to_receivertown = sent_data.get('to_town'),
                # from_personname = sent_data.get('from_personname'),
                from_countries = sent_data.get('from_countries'),
                from_town = sent_data.get('from_town'),
                to_countries = sent_data.get('to_countries'),
                to_town = sent_data.get('to_town'),
                package_kind = sent_data.get('package_kind'),
                quantity = sent_data.get('quantity'),
                description = sent_data.get('description'),
                weight  = sent_data.get('weight'),
                length = sent_data.get('length'),
                width = sent_data.get('width'),
                height = sent_data.get('height'),
                airfreight_charges = sent_data.get('airfreight_charges'),
                other_charges = sent_data.get('other_charges'),
                insur_amount = sent_data.get('insur_amount'),
                nvd = sent_data.get('nvd'),
                ncv = sent_data.get('ncv'),
                handling_info = sent_data.get('handling_info'),
                user_saved_by_id = '1'
            ).save()

            invoice_p = InvoiceLetter.objects.get(inv_id=id)
            invoice_p.is_processed = True
            invoice_p.save()

            messages.success(request, "The Airway bill has been added successfully")

        except Exception as e:
            print(f"Error saving the data:  {e}")
            messages.error(request, f"The Airway bill did not save {e}")

        
        return redirect('dashboard-products')
    else:
        invoicedatas = inv_id_f.values()
        print(invoicedatas)
        data = {}
        for invoice in invoicedatas:
            for inv in invoice:
                data[inv]=invoice.get(inv)

        print(data)
        form = Airwaybill(data=data)

        context = {
            'form': form,

        }

        return render(request, 'services/airwaybill.html', context)


def print_invoice(request, id):
    sales = [
        {"item": "Keyboard", "amount": "$120,00"},
        {"item": "Mouse", "amount": "$10,00"},
        {"item": "House", "amount": "$1 000 000,00"},
    ]
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)

    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')


def generateAirwaybill(request, id):
    sales = [
        {"item": "Keyboard", "amount": "$120,00"},
        {"item": "Mouse", "amount": "$10,00"},
        {"item": "House", "amount": "$1 000 000,00"},
    ]
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)

    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')