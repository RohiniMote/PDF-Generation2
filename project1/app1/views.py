from django.shortcuts import render
from app1.models import Employee
from app1.utils import render_to_pdf


# Create your views here.

def ResultList(request):
    template_name = "pdf.html"
    records = Employee.objects.all().order_by("eid")

    return render_to_pdf(
        template_name,
        {
            "record": records,
        },
    )


