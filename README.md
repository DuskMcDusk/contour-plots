# Contour plots

## Task list

- Create functions to convert the data into the desired values
- Test conversions
- convert the .xyz files into .csv with the approprieate data and names
- plot a *contour plot* for every set of data

### Data conversions

The first column in the .xyz file is the angle 2T (theta).

To convert the first column(X) we use the formula

`M = arcsin( (1.54/0.413) * sin(radians(2theta))/2 )`

gives us the angle in radians. Next the radians are converted into degrees using `degrees(2M)`

The second column int the file .xyz is the intensity.
To convert the second coulmn(Y) take the MAX value in the column and divide every value by MAX