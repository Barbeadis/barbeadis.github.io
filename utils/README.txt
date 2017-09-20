== barbeadis.it ==

si basa su nikola


== barbeadis.info ==

GoDaddy:

* dominio barbeadis.info fino al 26/08/2016 € 3,13

== Digital Ocean ==

rsync -r barbeadis.info/* 162.243.254.187:/var/www/barbeadis.info/public_html


== per generare la favicon ==

    http://www.favicon-generator.org/


== Vecchio support Amazon ==

Amazon buckets:

* barbeadis.info
* logs.barbeadis.info
* www.barbeadis.info

DNS:

    dig www.barbeadis.info
    dig barbeadis.info
    dig barbeadis.info NS
    dig -t a barbeadis.info @ns-301.awsdns-37.com


== setup aws cli ==

    pip install awscli
    aws configure
    # cat ~/.aws/config
    # cat ~/.aws/credentials
    # assegnare la policy AdministratorAccess
    aws s3 ls s3://barbeadis.info


== rilascio dei file ==

    cd ~/Projects/barbeadis
    python scale_down.py

    cd barbeadis.info
    aws s3 sync . s3://barbeadis.info


== recupero dei log ==

    cd ~/Projects/barbeadis
    aws s3 sync s3://logs.barbeadis.info logs.barbeadis.info/
