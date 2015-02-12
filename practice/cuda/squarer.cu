#include <stdio.h>

//no return type means that we store all information into the pointers 
__global__ void square(float *d_out, float *d_in) {
    //threadIdx is the index of the thread
    // this is how the thread knows its id.
    int globalId = threadIdx.x;
    float f = d_in[globalId];
    d_out[globalId] = f * f;
}

int main(int argc, char ** argv) {
    const int ARRAY_SIZE = 64;
    const int ARRAY_BYTES = ARRAY_SIZE * sizeof(float);
    
    
    
    //this loop initializes an array of ARRAY_SIZE
    float h_in[ARRAY_SIZE];
    for ( int i = 0; i < ARRAY_SIZE; i++ ) {
        h_in[i] = float(i);
    }
    
    float h_out[ARRAY_SIZE];
    
    // declare GPU memory pointers
    // this allows us to know the address of our data on the GPU
    float * d_in;
    float * d_out;
    
    // allocate GPU memory
    cudaMalloc((void**) &d_in, ARRAY_BYTES);
    cudaMalloc((void**) &d_out, ARRAY_BYTES);
    
    // transfer the array to the GPU
    cudaMemcpy(d_in, h_in, ARRAY_BYTES, cudaMemcpyHostToDevice);
    
    // launch the kernel, node the <<<>>>
    // ARRAY_SIZE indicates the number of cores we want to use.
    square<<<1, ARRAY_SIZE>>>(d_out, d_in);
    
    // transfer the array from GPU to the CPU
    cudaMemcpy(h_out, d_out, ARRAY_BYTES, cudaMemcpyDeviceToHost);
    
    //cleaning up memory
    cudaFree(d_in);
    cudaFree(d_out);
    
    //print the array:
    
    for ( int i = 0; i < ARRAY_SIZE; i++ ) {
        printf("%f", h_out[i]);
        printf( ( ( i%4 ) != 3 ) ? "\t" : "\n");
    }
    
    return 0;
}