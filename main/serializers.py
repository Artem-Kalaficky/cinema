import json
import datetime


def serialize(queryset):
    offset = datetime.timedelta(hours=3, minutes=0)
    json_data = json.loads(json.dumps([{'time': (obj.time + offset).strftime("%H:%M"),
                                        'film': obj.film.name,
                                        'hall': obj.hall.hall_number,
                                        'hall_id': obj.hall.id,
                                        'cost': obj.cost,
                                        'pk': obj.id,
                                        'film_id': obj.film.id} for obj in queryset]))
    return json_data


def serialize_for_film(queryset):
    offset = datetime.timedelta(hours=3, minutes=0)
    json_data = json.loads(json.dumps([{'time': (obj.time + offset).strftime("%H:%M"),
                                        'hall': obj.hall.hall_number,
                                        'pk': obj.id} for obj in queryset]))
    return json_data


def serialize_for_ticket(queryset):
    json_data = json.loads(json.dumps([{'place': obj.place,
                                        'row': obj.row} for obj in queryset]))
    return json_data

