clc; clear all; close all;

HEADER = ['FRAME_ID','Q1','A1_1','A1_2','A1_3','Q2','A2_1','A2_2','A2_3',...
          'Q3','A3_1','A3_2','A3_3','Q4','A4_1','A4_2','A4_3',...
          'Q5','A5_1','A5_2','A5_3'];
QUESTION = ['Q1','Q2','Q3','Q4','Q5'];
ANSWER = ['A1_1','A1_2','A1_3','A2_1','A2_2','A2_3','A3_1','A3_2','A3_3',...
          'A4_1','A4_2','A4_3','A5_1','A5_2','A5_3'];

traindatas = load('datas\train.mat');
answers = cat(2,traindatas.A1_1,traindatas.A1_2,traindatas.A1_3,...
                traindatas.A2_1,traindatas.A2_2,traindatas.A2_3,...
                traindatas.A3_1,traindatas.A3_2,traindatas.A3_3,...
                traindatas.A4_1,traindatas.A4_2,traindatas.A4_3,...
                traindatas.A5_1,traindatas.A5_2,traindatas.A5_3);
[N_FRAME,tmp_] = size(traindatas.Frame_id);

%%%% qustion1 : standing or sitting
line_standing = [];
line_sitting = [];
line_noq1 = [];
for i = 1:N_FRAME
    if any(ismember(answers(i,:), 'standing')) 
        n_=length(line_standing);
        line_standing(n_+1)=i;
    elseif any(ismember(answers(i,:), 'sitting'))
        n_=length(line_sitting);
        line_sitting(n_+1)=i;
    else
        n_=length(line_noq1);
        line_noq1(n_+1)=i;
    end
end