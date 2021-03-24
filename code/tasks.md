

- create a class called capybara_pair which has youngest and oldest capybara (both capybara objects)

- write a function that reads capybara csv and returns average capybara age
- 
#optional
- write a function that gets a list of csv files and a new name for a new csv file, then write a function concat_capis that willtake all capybars from all csv files and put in a new csv
-- function header `def concat_capis(in_filenames, out_filename):`
-- example calls: `concat_capis(["capis1.csv", "capis2.csv"], "all-capis.csv")`
- given a folder, write a function that will gonna search recursively through all the subfolders and grab all files with .csv extension and return the paths to the files in a list
- plot capybara age distribution using seaborn
- read about python doc string

#done
- write function called write_capybaras that creates capybara csv
- write function that reads capybara csv and returns capybara object with the longest name
- write function that reads from capybara csv and returns theyoungest and the oldest capybara

#new
- make a capybara dataset class that contains a list of capybara and a member function to write the dataset to the file and read the dataset from the file
- create a constructor for capybara dataset class that takes a path to the file and constructs the object