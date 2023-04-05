from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.generic.database import SQL
from diagrams.azure.compute import VM
from diagrams.generic.os import Windows
from diagrams.generic.storage import Storage as Blank
from diagrams.azure.database import DatabaseForPostgresqlServers as Postgres
from diagrams.programming.framework import Django

graph_attr = {
    'fontsize': '36'
}

node_attr = {
    'fontsize': '18'
}

with Diagram('BAPI WebApp', show='False', graph_attr=graph_attr, node_attr=node_attr):
    with Cluster('Production'):
        vm = VM('Ubuntu 16.04 VM')
        postgres = Postgres('Azure Database for PostgreSQL')  
        vm - postgres - Django('django')
    with Cluster('Development'):
       wsl2 = Blank('WSL2')
       Windows('Windows 10') - wsl2        

    wsl2 >> vm
    wsl2 >> postgres

#with Diagram('Development', show='False'):
#    Windows('Windows 10') >> Blank('WSL2')

'''
with Diagram("Workers", show=False, direction="TB"):
    lb = ELB("lb")
    db = RDS("events")
    lb >> EC2("worker1") >> db
    lb >> EC2("worker2") >> db
    lb >> EC2("worker3") >> db
    lb >> EC2("worker4") >> db
    lb >> EC2("worker5") >> db
'''

'''
with Diagram("Grouped Workers", show=False, direction="TB"):
    ELB("lb") >> [EC2("worker1"),
                  EC2("worker2"),
                  EC2("worker3"),
                  EC2("worker4"),
                  EC2("worker5")] >> RDS("events")
'''