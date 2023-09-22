import os
import reports_backend as backend                                                                                                       
import reports_frontend as frontend                                                                                                     
                                                                                                                                                  
class MainApp:                                                                                                                                  
    @staticmethod                                                                                                                               
    def run_backend():                                                                                                                          
        backend.main()                                                                                                                          
                                                                                                                                                
    @staticmethod                                                                                                                               
    def run_frontend():                                                                                                                         
        frontend.main()                                                                                                                         
                                                                                                                                                
app = MainApp()                                                                                                                                 
app.run_backend()                                                                                                                               
app.run_frontend() 
