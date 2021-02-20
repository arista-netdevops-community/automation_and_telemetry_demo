import yaml
from jinja2 import Template
import os 

with open('input.yml') as f:
  data = yaml.load(f.read(), yaml.FullLoader)

# generate docker-compose.yml file for a TIG stack

with open('templates/docker-compose.j2') as f:
  template = Template(f.read())

conf=open("docker-compose.yml",'w')
conf.write(template.render(data))
conf.close()

# delete telegraf conf file for old devices

dir = 'telegraf.d'
for i in os.listdir(dir):
    if i not in ["output.conf","processor.conf"]: 
        os.remove('{}/{}'.format(dir,i))

# generate a telegraf conf file for each device

with open('templates/telegraf_conf_dev.j2') as f:
  template = Template(f.read())

for dev in data['telegraf']['devices']:
  output_file = dir +'/' + dev + '.conf'
  conf=open(output_file,'w')
  conf.write(template.render(data, device=dev))
  conf.close()
