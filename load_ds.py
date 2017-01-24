from google.cloud import datastore as ds

ds_client = ds.Client()

kind = 'Product'
id='hey it works'
task_key = ds_client.key(kind, id)
task = ds.Entity(key=task_key)
task['product-name'] = 'lenovo pos'

ds_client.put(task)

print('we did it!')