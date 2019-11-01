import logging
import azure.functions as func
#from HttpTrigger.IdentifyFile import identify_file
from HttpTrigger.test import choose

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
            choose("hi!"),
            #identify_file("d0d0357f065e42b382085cebe48f042c","/Users/keonmin/voice1/RandomGuyLong.wav", NULL, "(32eb9781-9d79-43bd-94e2-ee3f0828d056,87e616cf-5bf3-4400-ab27-ed12c4b3985d,a491a0cb-41d6-4334-992c-06ef70246fc1,fbf5086b-da62-486e-8daa-72433a3f5885)"),
            status_code=400
        )
