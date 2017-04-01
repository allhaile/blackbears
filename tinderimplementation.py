from datetime import datetime

class User(object):
	def __init__(self, data_dict):
		self.data = data_dict

	def user_id(self):
		return self.data["__id"]

	def age(self):
		userAge = self.data.get("birth_date")
		if userAge:
			d = datetime.strptime(raw, '%Y-%m-%dT%H:%M:%S.%fZ')
			#
            return datetime.now().year - int(d.strftime('%Y'))

