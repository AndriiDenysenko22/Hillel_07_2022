st_ring_in_bytes = b'r\xc3\xa9sum\xc3\xa9'
print('Вхідний рядок: ', st_ring_in_bytes)

de_co_de_st_ring = st_ring_in_bytes.decode()

print('-'*50)
print('Декодований рядок: ', de_co_de_st_ring)

en_coded_string = de_co_de_st_ring.encode('Latin1')

print('-'*50)
print('Закодований в Latin1 рядок: ', en_coded_string)

decoded_from_Latin_1_string = en_coded_string.decode('Latin1')

print('-'*50)
print('Декодований із Latin1 рядок: ', decoded_from_Latin_1_string)
