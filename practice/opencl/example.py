import pyopencl as cl
import numpy

class CL:
	def __init__(self):
		self.context = cl.create_some_context()
		self.queue = cl.CommandQueue(self.context)

	def loadProgram(self, filename):
		# read OpenCL file into a string
		f = open(filename, 'r')
		kernel = "".join(f.readlines())
		print kernel
		#build the program
		self.program = cl.Program(self.context, kernel).build()

	def popCorn(self):
		mf = cl.mem_flags

		#initialize CPU arrays
		self.a = numpy.array(range(10), dtype=numpy.float32)
		self.b = numpy.array(range(10), dtype=numpy.float32)

		#create GPU buffers (OPENCL)
		self.a_buf = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.a)
		self.b_buf = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.b)
		self.dest_buf = cl.Buffer(self.ctx, mf.WRITE_ONLY, self.b.nbytes)

	def execute(self):
		#a method matching our file has been added to our program
		#we pass in the command queue, global worksize, local work size, and our variables
		self.program.kern(self.queue, self.a.shape, None, self.a_buf, self.b_buf, self.dest_buf)
		result = numpy.empty_like(self.a)
		cl.enqueue_read_buffer(self.queue, self.dest_buf, result).wait()
		print 'a', self.a
		print 'b', self.b
		print 'c', c

if __name__ == '__main__':
	example = CL()
	example.loadProgram("kern.cl")
	example.popCorn()
	example.execute()
