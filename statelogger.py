import numpy as 	np
import matplotlib
import logging
import os

class statelogger():
	
	def __init__(self,filename,*args):
		self.no_variables = len(args);
		self.filename = filename+str('.npy');
		self.statenumber = 1;
		self.all_states = []
		
		self.logfile = 'statevar.log'
		
		a = open(self.logfile,'w+')
		a.close()
		
		
		self.logger = logging.getLogger("statelogger")
		
		
		self.logger.setLevel(logging.INFO) #Set to Debug only to print every function call
		
		
		self.fh = logging.FileHandler(self.logfile)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.fh.setFormatter(formatter)
		self.logger.addHandler(self.fh)
		
		self.logger.info('**********STARTING***********')
		self.logger.info('Logging to - *' + str(self.logfile) + '*')
		self.logger.info('Recieved ' + str(self.no_variables) + ' variables')
		self.logger.info('Starting Recording')

		self.current_state = []
		
		
		for i in range(len(args)):
			self.current_state.append(np.array(args[i]));
		
		self.all_states = self.current_state
		
		self.logger.info('Initialization Finished')
		
	def update_data(self):
		logger_update_data = self.logger.getChild('update_data')
		
		for i in range(self.no_variables):
			self.all_states[i] = np.vstack((self.all_states[i],self.current_state[i]))
		logger_update_data.debug('Data Update successful')

			
	def write_to_file(self):
		logger_write_to_file  = self.logger.getChild('write_to_file')
		
		np.save(self.filename,self.all_states)
		logger_write_to_file.debug('Written to file succesfully')

		
			
	def add_state(self,*args):
		logger_new_state = self.logger.getChild('add_state')
		
		logger_new_state.info('Recieved %s variables.' %(len(args)))
		self.statenumber = self.statenumber+1
		self.current_state = [];
		
		try:
			for i in range(len(args)):
				self.current_state.append(np.array(args[i]));
			self.update_data()
		except(ValueError,IndexError):
			print('Inputted number of variables does not meet exisiting bank requirement');
			logger_new_state.error('Inputted number of variables does not meet exisiting bank requirement')
		else:
			self.write_to_file()
			logger_new_state.info('Added %s variables to bank' %(len(args)))
	def close_logger(self):
		self.logger.info('**********FINISEHD***********')
		
		self.logger.removeHandler(self.fh)
		
	#def report_log_io():
		
			
		
		
		