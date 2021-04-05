import helper as h

sessionidentifier = h.get_sessionidentifier(h.get_sessiontoken())

#Use to get your tenantid for future calls

h.get_tenantid(sessionidentifier)    

#A sample call that you can run after getting the tenant id

#h.get_applications(sessionidentifier)

#Use this to see the fingerprints of your certificates

h.get_certificates(sessionidentifier)

#Uploads the certificate, also outputs the fingerprint which you will need later if deleting a certificate

#h.upload_certificate(sessionidentifier)

#h.upload_multiple_certificate(sessionidentifier)

#Deletes the certificate

#h.delete_certificate(sessionidentifier)



