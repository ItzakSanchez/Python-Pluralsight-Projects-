from dataclasses import dataclass
from handlers import handler_chain

@dataclass
class Request:
    request_type: str
    request_details: str

REQUESTS = [
    Request("dogs", "walk twice a day"),
    Request("cats", "A new cat request")
]

for r in REQUESTS:
    handler_chain.handle(r)