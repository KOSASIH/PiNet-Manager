# network_config.py
import ncclient

# Create Netconf client
client = ncclient.manager.connect(host='example.com', port=830, username='user', password='pass')

# Get device configuration
config = client.get_config(source='running')

# Edit configuration
config.edit_config(target='candidate', config='''<config>
    <interfaces>
        <interface>
            <name>eth0</name>
            <description>Example interface</description>
        </interface>
    </interfaces>
</config>''')

# Commit changes
client.commit()
