#!/usr/bin/python3

""" Base class for all the other classes """
from datetime import datetime
import uuid


class BaseModel:
	""" Base class for all models.

	Attributes:
		id (str) - assigned with an uuid when an instance is created
		created_at (datetime) - assigned with the current datetime when an instance is created
		updated_at (datetime) - assigned with the current datetime when an instance is created and it will be updated every time you change your object
	"""
	
	def __init__(self, *args, **kwargs):
		""" Initializes a new instance of BaseModel

		Args:
			*args: Variable length argument list
			**kwargs: Arbitrary keyword argument
		"""
		if kwargs:
			for key in kwargs.keys():
				if key == 'id':
					self.id = kwargs[key]
				elif key == 'created_at':
					self.created_at = datetime.fromisoformat(kwargs[key])
				elif key == 'updated_at':
					self.updated_at = datetime.fromisoformat(kwargs[key])
		else:
			self.id = str(uuid.uuid1())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
	
	def __str__(self):
		""" Returns:
			str: A string representation of the model instance.
		"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def name(self, arg):
		""" Sets the name attribute of the model instance.

		Args:
			arg: The value to set as the name attribute
		"""
		self.name = arg
	
	def my_number(self, arg):
		""" Sets the my_number attribute of the model instance.

		Args:
			arg: The value to set as the my_number attribute.
		"""
		self.my_number = arg
	
	def save(self):
		""" Updates the updated_at attribute of the model instance to the current time """
		self.updated_at = datetime.now()
	
	def to_dict(self):
		""" Returns:
			dict: A dictionary representatio of the model instance.
		"""
		d = self.__dict__
		d.update({'__class__': self.__class__.__name__})
		d['created_at'] = self.created_at.isoformat()
		d['updated_at'] = self.updated_at.isoformat()
		return d