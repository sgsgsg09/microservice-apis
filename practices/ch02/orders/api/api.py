from datetime import datetime
from uuid import UUID
from starlette.responses import Response
from starlette import status
from orders.app import app
order = {
	'id': 'ff0f1355-e821-4178-9567-550dec27a373',
	'status': "delivered",
	'created': datetime.utcnow(),
	'order': [
		{
			'product': 'cappuccino'
			'size': 'medium',
			'quantity': 1,
		}
	]
}

@app.get('/orders')
def get_orders():
    return {'orders': [order]}
