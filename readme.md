**Tasksyncer-python-client**

Serves as an interface to Tasksyncer
In the current version supports the steps associated with the polarion-sync

**Usage:**
- **Set data:** python main.py set --version VERSION KEY VALUE
- following keys should be set with appropriate values: ['hostname', 'project', 'polarion_url', 'column_names',
                'token1', 'token2', 'namespace', 'column_mapping_names',
                'column_mapping_trello', 'polarion_project', 'username',
                'password', 'test_cycle', 'ignore_titles']
- it is possible to save multiple sets of data using different --version options
- --version default plays a specific role, when the attributes for any version is not present,
    it is defaulted to the value in 'default' version
- **Get data** python main.py get data
- Shows the saved data in json format
- **Conduct sync** python main.py sync --version VERSION polarion
