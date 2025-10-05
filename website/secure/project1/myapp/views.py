from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
import os
import csv
from datetime import datetime

def index(request):
    if request.method == 'POST':
        text = request.POST.get('input_text', '')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Write to 1.txt (plain log)
        txt_path = os.path.join(os.path.dirname(__file__), '..', '1.txt')
        with open(txt_path, 'a') as f:
            f.write(f'{timestamp} - {text}\n')

        # Write to log.csv (structured log)
        csv_path = os.path.join(os.path.dirname(__file__), '..', 'log.csv')
        file_exists = os.path.isfile(csv_path)
        with open(csv_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(['Timestamp', 'Text'])  # Header row
            writer.writerow([timestamp, text])

        messages.success(request, '✅ Text saved to 1.txt and log.csv!')
        return HttpResponseRedirect('/')
    return render(request, 'myapp/index.html')