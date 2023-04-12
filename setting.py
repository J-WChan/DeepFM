import os 

file_path = './dataset/laptops.csv'
output_path = './output/laptops_output.csv'
drop_column = ['img_link','no_of_ratings','no_of_reviews']
sparse_column = ['name', 'processor', 'ram', 'os', 'storage']
dense_column = ['price(in Rs.)','display(in inch)']
target_column = 'rating'
