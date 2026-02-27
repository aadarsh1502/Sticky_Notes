from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Note

def LPU(req):
    notes = Note.objects.all()
    return render(req, "index.html", context={'notes':notes})

def aboutView(req):
    return render(req, "about.html")

def saveDataView(req):
    print(req.POST)
    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
        messages.error(req, "Fill all details")
        return redirect("/")

    note= Note(title = title, description= description)
    note.save()
    messages.success(req, "Detail saved")
    return redirect("/")
    # return HttpResponse(f"Details saved")

def delete(req, id):
    note= Note.objects.get(id=id)
    note.delete()
    messages.success(req, "Note deleted successgully")
    return redirect("/")
    # return HttpResponse("Delete Success" + str(id))

def updateViewpage(req, id):
    note = Note.objects.get(id=id)
    # value="{{note.title}}"
    # note.title = title
    note.save()
    return render(req, "edit-page.html", {"note": note})


def updateDataView(req, id):
    note = Note.objects.get(id=id)
    title = req.POST.get("title", "")
    description = req.POST.get("description", "")

    if not title or not description:
        messages.error(req, "Fill all details")
        return redirect(f"/update-note/{id}")

    note.title = title
    note.description = description
    note.save()

    messages.success(req, "Note Updated Successfully")
    return redirect("/")
    
# def aboutLPU(req):
#     return HttpResponse("Hello,  I'm great, thanks.")

# def aboutme(req):
#     return HttpResponse("Hii! I'm Aadarsh")