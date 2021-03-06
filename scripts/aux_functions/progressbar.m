% PROGRESSBAR shows progress in loops
%
% idx : int
%   current index
% step : int (0 to 100)
%   interval at which to show progress (in percentage)
% n_idx : int
%   upper limit of the loop for which progressbar is being shown
%
% AUTHOR: Mainak Jas
function progressbar(idx, step, n_idx)

    step_idx = floor(n_idx*step/100);

    if rem(idx, step_idx) == 0
        fprintf('.');
    end

    if idx == n_idx
        fprintf('\n')
    end

end