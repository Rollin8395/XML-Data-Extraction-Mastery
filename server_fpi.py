from xml.dom import minidom

report = minidom.parse(r'ADUReport.xml')
devices = report.getElementsByTagName('Device')
#data = str(devices[0].childNodes[0].data)

for i in devices:
    drive_name = i.getAttribute('marketingName')

    if 'Physical Drive' in drive_name:
        print (drive_name)
        data = i.getElementsByTagName('MetaProperty')
        for l in data:
            #print (l.getAttribute('id'))
            data_poh = l.getAttribute('id')
            if 'Power On Hours' in data_poh:
                poh = l.getAttribute('value')
                dec = int(poh, 16)
                print ('Power On Hours ' + str(dec))
            if 'Current Temperature' in data_poh:
                poh = l.getAttribute('value')
                dec = int(poh, 16)
                print ('Current Temperature '+ str(dec))
            if 'Seek Errors' in data_poh:
                poh = l.getAttribute('value')
                dec = int(poh, 16)
                print ('Seek Errors '+ str(dec))
            if 'Reallocation Sectors' in data_poh:
                poh = l.getAttribute('value')
                dec = int(poh, 16)
                print ('Reallocation Sectors '+ str(dec))
            if 'Bad Target Count' in data_poh:
                poh = l.getAttribute('value')
                dec = int(poh, 16)
                print ('Bad Target Count '+ str(dec))

    print ('------------------------------------------------')
        


'''
        meta_struct = i.getElementsByTagName('MetaStructure')
        for j in meta_struct:
            meta_prop_struct = i.getElementsByTagName('MetaPropertyStructure')
            for k in meta_prop_struct:
                data = i.getElementsByTagName('MetaProperty')
                for l in data:
                    #print (l.getAttribute('id'))
                    data_poh = l.getAttribute('id')
                    if 'Power On Hours' in data_poh:
                        poh = l.getAttribute('value')
                        dec = int(poh, 16)
                        print (dec)
'''
