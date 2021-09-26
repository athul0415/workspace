# workspace

vm_provision:

1) vm_provisioing playbook will provision a new VM with an Ubunutu OS with the help of AWS Cloud Formation Template.
2) Playbook also generates a dynamic inventory for the newly provisioned VM.
3) Login credentails for the provisioned VM is configured in the ansible controller and is vault protected
4) Playbook can be trigger with the below ansible command
   ansible-playbook vm_provision.yml --vault-password-file <path/to/vault/file>
   
install_app:

1) Host group of the target server is provided based on the dynamic inventory generated in the vm_provision playbook
2) With the execution of this playbook the JAVA and Jenkins apllication will be installed on the VM wich is provisoned in the earlier execution
3) Command to execute the playbook
   ansible-playbook install_app.yml -i /path/to/dynamic/inventory --vault-password-file <path/to/vault/file>
