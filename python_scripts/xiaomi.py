#/config/python_scripts/xiaomi.py
args = {"entity_id": "vacuum.xiaomi_vacuum_cleaner", "command" : "app_segment_clean", "params":  []}
params_lera = data.get("input_boolean.lera_vacuum")
params_artem = data.get("input_boolean.artem_vacuum")
params_kitchen = data.get("input_boolean.kitchen_vacuum")
params_koridor = data.get("input_boolean.koridor_vacuum")
params_spalnya = data.get("input_boolean.spalnya_vacuum")
params_zal = data.get("input_boolean.zal_vacuum")
if params_lera == 'on':
  args["params"].extend([20])
if params_artem == 'on':
  args["params"].extend([19])
if params_kitchen == 'on':
  args["params"].extend([16])
if params_koridor == 'on':
  args["params"].extend([17])
if params_spalnya == 'on':
  args["params"].extend([18])
if params_zal == 'on':
  args["params"].extend([21])
hass.services.call('vacuum', 'send_command', args)
