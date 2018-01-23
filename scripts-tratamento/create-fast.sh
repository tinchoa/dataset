                                    
#!/bin/bash                         
                                    
saida=/home/dataset/fast-24.log     
                                    
for i in `cat folders`; do          
        echo 'analyzing ' $i        
        cat $i/fast.log  >>$saida   
        echo 'entering folder '$f   
done;                               
                                    
                                    
                                    