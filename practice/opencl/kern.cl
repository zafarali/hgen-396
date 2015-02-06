__kernel void kern(__global float* a, __global float* b, __global float* result){
	unsigned int i = get_global_id(0);
	result[i] = a[i] + b[i];
}