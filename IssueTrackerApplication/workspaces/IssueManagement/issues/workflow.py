from ..packages.workflow.base.engine import WorkflowBase    
from .models import Issue

class IssueWorkflow(WorkflowBase):
    status_transitions = [
        {
            "name": "start_progress",
            "display_name": "Start Progress",
            "description": "Move issue from Open to In Progress",
            "confirmation_message": "Are you sure you want to start working on this issue?",
            "from": "open",
            "to": "in_progress"
        },
        {
            "name": "resolve",
            "display_name": "Resolve Issue",
            "description": "Mark issue as resolved",
            "confirmation_message": "Are you sure you want to resolve this issue?",
            "from": "in_progress",
            "to": "resolved",
        },
        {
            "name": "reopen",
            "display_name": "Reopen Issue",
            "description": "Move issue back to Open",
            "confirmation_message": "Are you sure you want to reopen this issue?",
            "from": "resolved",
            "to": "open",
        }
    ]
    ###  Transition Conditions ###
    def start_progess_condition(self, request, object_instance, **kwargs):
        return object_instance.status == "open"
    def resolved_condition(self, request, object_instance, **kwargs):
        return object_instance.status == "in_progess" 
    def reopen_condition(self, request, object_instance, **kwargs):
        return object_instance.status == "resolved"
    
    ### Processing Methods ###
    def start_progress_done(self, request, object_instance, transaction_obj):
        object_instance.status = "in_progress"
        print(object_instance.assignee)
        object_instance.save()
        

    def resolve_done(self, request, object_instance, transaction_obj):
        object_instance.status = "resolved"
        object_instance.save()
        
    def reopen_done(self, request, object_instance, transaction_obj):
        object_instance.status = "open"
        object_instance.save()
        

    class Meta:
        model = Issue
        statuses={
            "open":{
                "color":"#FF4C4C",
                "label":"Open"
            },
             "in_progress":{
                "color":"#FFC107",
                "label":"In Progress"
            },
             "resolved":{
                "color":"#4CAF50",
                "label":"Resolved"
            }

        }
        on_create_status = "open"