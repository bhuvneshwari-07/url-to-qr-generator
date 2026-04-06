import qrcode
import io
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import QRCodeData

def input_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')

        if name and url:
            qr = qrcode.make(url)
            buffer = io.BytesIO()
            qr.save(buffer, format='PNG')

            qr_data = QRCodeData(name=name, url=url)
            qr_data.qr_image.save(f"{name}.png", ContentFile(buffer.getvalue()), save=True)
            qr_data.save()

            return redirect('result', qr_id=qr_data.id)
        else:
            messages.error(request, "Please enter both Name and URL.")
    return render(request, 'qr_app/input.html')


def result_page(request, qr_id):
    qr_data = get_object_or_404(QRCodeData, id=qr_id)
    return render(request, 'qr_app/result.html', {'qr': qr_data})


def dashboard(request):
    qr_codes = QRCodeData.objects.all().order_by('-created_at')
    last_qr = qr_codes.first() if qr_codes.exists() else None
    return render(request, 'qr_app/dashboard.html', {'qr_codes': qr_codes, 'last_qr': last_qr})


def delete_qr(request, qr_id):
    qr = get_object_or_404(QRCodeData, id=qr_id)
    qr.delete()
    messages.success(request, f"QR Code '{qr.name}' deleted successfully!")
    return redirect('dashboard')


#  {% comment %} project name - scanner, app name -  mobile , environment name - env {% endcomment %}