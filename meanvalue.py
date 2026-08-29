"""Mean of 40 numbers is 38. Later on it was detected that number 56 was misread as 36.
Find the correct mean."""
mean1=38
wrongno=36
correctno=56
totalno=40
sum=mean1*totalno
print("The sum of 40 numbers is:", sum)
no2=sum-((wrongno)-(correctno))
mean2=no2/totalno
print("Corrected mean is:", mean2)