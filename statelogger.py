import numpy
import matplotlib
import logging


class statelogger():
	
	def __init__(self,filename,*args):
		self.no_variables = len(args);
		self.filename = filename+str('.npy');
		self.statenumber = 1;
		self.all_states = []
		self.logger = logging.getLogger("StateVariable Logger")
		self.logger.setLevel(logging.INFO)

    # create the logging file handler
		fh = logging.FileHandler("statevar.log")

		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		fh.setFormatter(formatter)

    # add handler to logger object
		self.logger.addHandler(fh)
		self.logger.info('Recieved ' + str(self.no_variables) + ' variables')
		self.logger.info('Starting Recording')

		self.current_state = []
		for i in range(len(args)):
			self.current_state.append(np.array(args[i]));
			#self.logger.info('Initiaez')
		
		self.logger.info('Initialization Finished')
		
	def update_data(self):
		for i in range(self.no_variables):
			self.all_states[i] = np.vstack((self.all_states[i],self.current_state[i]))
			
	def write_to_file(self):
		np.save(self.filename,self.all_data)
			
	def add_state(self,*args):
		logger = logging.getLogger('statelogger.add_state')
		logger.info('Recieved %s variables. Appending state.' len(args))
		self.statenumber =+1
		self.current_state = [];
		for i in range(len(args)):
			self.current_state.append(np.array(args[i]));
		self.update_data();
		self.write_to_file()
		logger.info('Added State completely')
	
		
	def report_log_io():
		
			
		
		
		