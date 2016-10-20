import ChongQing.mysql_part

print(ChongQing.mysql_part.last_id())
last_id = ChongQing.mysql_part.last_id()
ChongQing.mysql_part.check_new_data(from_id=last_id)
