% This is an implementation of the Q-potts model found at http://users.minet.uni-jena.de/~ullrich/matlab/potts.html


function sigma = Potts(N,q,beta,start,stps) 
% POTTS(N,Q,BETA,START,STPS) initializes and 
%   iterates a Potts configuration for the given values.
%   N - number of rows of the lattice
%   BETA - inverse temperatur times interaction strength
%       ( log(1+sqrt(q)) is the critical temperature )
%   START - 0 for random initial configuration 
%           k for constant k initial conf. (k = 1,...,q)
%   STPS - number of iterations
%
%   e.g. Potts(200,8,log(1+sqrt(8)),0,10000)


randTol = 1;

%% Control the input arguments
if N/2 ~= ceil(N/2)
    warning('MATLAB:paramAmbiguous','N must be even! Set N = N+1.');
    N=N+1;
end
if start ~= round(start) || start > q || start < 0
    error('START value not valid!')
end



%% Initial spin configuration
if start == 0
    sigma = randi(q,N); 
else 
    sigma = start*ones(N);
end



%% Evolve the system for a fixed number of steps 
%stps=5000;
for i=1:stps, 
    
% %% Metropolis Step (single spin update)
%     % Coordinate to change
%     x = randi(N^2);
%     coord(1) = mod(x-1,N)+1; 
%     coord(2) = ceil(x/N);
% 
%     % Calculate number of neighbored nodes unequal to the spin of the node
%     spin = sigma(coord(1),coord(2));
%     neighbors = (spin~=sigma(mod(coord(1)-2,N)+1, coord(2))) + ...
%             (spin~=sigma(coord(1), mod(coord(2),N)+1)) + ...
%             (spin~=sigma(mod(coord(1),N)+1, coord(2))) + ...
%             (spin~=sigma(coord(1), mod(coord(2)-2,N)+1));
% 
%     spin_new = randi(q);
%     neighbors_new = (spin_new~=sigma(mod(coord(1)-2,N)+1, coord(2))) + ...
%             (spin_new~=sigma(coord(1), mod(coord(2),N)+1)) + ...
%             (spin_new~=sigma(mod(coord(1),N)+1, coord(2))) + ...
%             (spin_new~=sigma(coord(1), mod(coord(2)-2,N)+1));
%         
%     % Calculate the transition probabilities 
%     p = exp(beta*(neighbors-neighbors_new)); 
% 
%     % Make the step
%     if rand() < p
%         sigma(coord(1),coord(2)) = spin_new;
%     end
%     
    
    %% Sweep algorithm
    % Change first a chessboard and the the complement
    for choice = 0:1

        chess = (circshift(repmat(eye(2),ceil(N/2),ceil(N/2)),[0 choice]));
        spins_new = randi(q,N);
        sigma_new = (1-chess).*sigma + chess.*spins_new;
        
        % Calculate number of neighbored nodes unequal to the spin of all nodes
        
        neighbors = (sigma==circshift(sigma, [ 0 1])) + ... 
            (sigma==circshift(sigma, [ 0 -1])) + ... 
            (sigma==circshift(sigma, [ 1 0])) + ... 
            (sigma==circshift(sigma, [-1 0])); 
        
        neighbors_new = (sigma_new==circshift(sigma_new, [ 0 1])) + ... 
            (sigma_new==circshift(sigma_new, [ 0 -1])) + ... 
            (sigma_new==circshift(sigma_new, [ 1 0])) + ... 
            (sigma_new==circshift(sigma_new, [-1 0])); 

        % Calculate the change in energy of flipping a spin 
    %     DeltaE = 2 .* neighbors + 4 + 2 .* B .* sigma; 
    %     DeltaE = 2*sigma .* neighbors + 2 .* B .* sigma;
    %    DeltaE = 2 * sigma .* neighbors; %(critical value for beta = 0.4406868)
        % DeltaE = sigma .* neighbors;  %(critical value for beta = 0.8813736)

        % Calculate the transition probabilities 
        p = exp(-beta*(neighbors-neighbors_new));

        % Decide which transitions will occur 
        %transitions = (U < p ).*(rand(N) < randTol) * -2 + 1; 
        transitions = (rand(N) < p ).* (rand(N) < randTol) .*... 
          chess .* (spins_new - sigma);

        % Perform the transitions  
            sigma = sigma + transitions;
    end
%     
    %% Plot the Ising state

    plot_title = sprintf('%dx%d Potts model with %d spins',N,N,q);

    %image((sigma-1)*(100/q));
    image(sigma)
    
    title(plot_title)
    text = sprintf('Step = %d',i);
    xlabel(text,'Color','k')
    set(gca,'YTickLabel',[],'XTickLabel',[],'XTick',[],'YTick',[]); 
    axis square; 
    
    %colormap(bone(q))
    %colormap(jet(2*q));
    %colormap(autumn(q+2));
    %colormap(hot(q+2));
    %colormap(summer(q))
    colormap(cool(q+5))
    %colormap(winter(q))
    
    drawnow;
    
end 


