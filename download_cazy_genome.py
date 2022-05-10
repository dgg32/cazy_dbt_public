import sys, re
import requests
from threading import Thread
import queue
from pyphy import pyphy

from threading import Semaphore
writeLock = Semaphore(value=1)

rx = re.compile(r'<td class="classe" id="navigationtab2"><a href="http://www\.cazy\.org/(\w+)\.html" class="nav2"><div class="famille">\w+</div></a><div class="nombre_de">(\d+)</div></td>')


roots = {
    "bacteria": "http://www.cazy.org/b",
    "eukaryote": "http://www.cazy.org/e",
    "archaea": "http://www.cazy.org/a",
    "virus": "http://www.cazy.org/v"
}

#scheme


in_queue = queue.Queue()
desired_ranks = ["superkingdom", "phylum", "class", "order", "family", "genus", "species"]

desired_ranks = ["superkingdom", "phylum", "class", "order", "family", "genus", "species"]

def work():
    while True:
        url = in_queue.get()

        
        
        content = requests.get(url).content.decode('iso8859-1')
        

        #try:
            
        container = {}
        
                #container["organism"] = re.findall(r'id="font_org">(.+)</font>', content)[0]
        cazy_page_taxon_name = re.findall(r'<font class="titre_cazome" id="font_org">(.+)<\/font>', content)[0]

        taxonomy_id = re.findall(r'http://www\.ncbi\.nlm\.nih\.gov/Taxonomy/Browser/wwwtax\.cgi\?id=(\d+)', content)[0]

        current_id = int(taxonomy_id)
        while current_id != 1 and current_id != -1:
            current_id = int(pyphy.getParentByTaxid(current_id))
            if pyphy.getRankByTaxid(current_id) in desired_ranks:
                container[pyphy.getRankByTaxid(current_id)] = [pyphy.getNameByTaxid(current_id), current_id]

        taxon_str = ",".join([f'"{container[x]}"' if x in container else "" for x in desired_ranks])

        writeLock.acquire()

        print (f'"{cazy_page_taxon_name}","{taxonomy_id}",{taxon_str}')
        writeLock.release()
            
<<<<<<< HEAD
=======
            
                    #container["organism"] = re.findall(r'id="font_org">(.+)</font>', content)[0]
        cazy_page_taxon_name = re.findall(r'<font class="titre_cazome" id="font_org">(.+)<\/font>', content)[0]

        taxonomy_id = re.findall(r'http://www\.ncbi\.nlm\.nih\.gov/Taxonomy/Browser/wwwtax\.cgi\?id=(\d+)', content)[0]

        container = {}

        current_id = int(taxonomy_id)
        while current_id != 1 and current_id != -1:
            current_id = int(pyphy.getParentByTaxid(current_id))
            if pyphy.getRankByTaxid(current_id) in desired_ranks:
                container[pyphy.getRankByTaxid(current_id)] = [pyphy.getNameByTaxid(current_id), current_id]

        tax_str = ",".join([f'"{container[x][0]}"' if x in container else '' for x in desired_ranks]) 
        writeLock.acquire()

        print (f'"{cazy_page_taxon_name}","{taxonomy_id}",' + tax_str)
        writeLock.release()
            
>>>>>>> fdaed0896df4821b7f84918bedcb803e18db44e1
        #except Exception:
        #    pass

        
        in_queue.task_done()

for i in range(7):
    t = Thread(target=work)
    t.daemon = True
    t.start()

<<<<<<< HEAD
print ('NAME,TAXID,' + ",".join(desired_ranks))
=======
print ('NAME,TAXID,' + ",".join([x.upper() for x in desired_ranks]))
>>>>>>> fdaed0896df4821b7f84918bedcb803e18db44e1
for root in roots.keys():
    root_initials = [x for x in re.findall(roots[root] + "\\w.html", requests.get(roots[root] + ".html").content.decode('iso8859-1'))]
    for root_initial in root_initials:
        genomes = [y for y in re.findall(roots[root] + "\\d+.html", requests.get(root_initial).content.decode('iso8859-1'))]
        for genome in genomes:
            in_queue.put(genome)
            
in_queue.join()