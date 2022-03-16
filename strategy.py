
import string
import random
from typing import List

def generate_id(length=8):
    #function for generating id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class SupportTicket:
    id: str
    customer: str
    issue: str
    
    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue
        
class CustomerSupport:
    tickets: List[SupportTicket] = []
    
    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer,issue))
                            
    def process_tickets(self, processing_strategy: str = "fifo"):
        #if it's empty, don't do anything
        if len(self.tickets)==0:
            print("There are no tickets to process.")
            return
        
        if processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)
                
    def process_ticket(self,ticket: SupportTicket):
        print(f"processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        
#create the application
app = CustomerSupport()

#register
app.create_ticket("Jon Smith", "bla bla bla")
app.create_ticket("Linus", "Hi need help")
app.create_ticket("Arjan", "it is not working")

#process the tickets
app.process_tickets("fifo")

        