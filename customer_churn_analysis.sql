CREATE TABLE dbo.CustomerChurnData (
    CustomerID INT,
    Age INT,
    Gender VARCHAR(20),
    Tenure INT,
    UsageFrequency INT,
    SupportCalls INT,
    PaymentDelay INT,
    SubscriptionType VARCHAR(30),
    ContractLength VARCHAR(30),
    TotalSpend DECIMAL(12,2),
    LastInteraction INT,
    Churn INT
);

SELECT
    COUNT(*) AS TotalCustomers,
    COUNT(DISTINCT CustomerID) AS UniqueCustomers
FROM [dbo].[customer_churn_dataset-testing-master];

SELECT  
    churn,
    COUNT(*) as customerCount
from [dbo].[customer_churn_dataset-testing-master]
GROUP BY Churn 
ORDER BY churn; 

SELECT 
    gender,
    churn,
    COUNT(*) as customerCount
from [dbo].[customer_churn_dataset-testing-master]
GROUP BY gender, churn 
ORDER BY gender, churn;

SELECT
    Gender,
    COUNT(*) AS TotalCustomers,
    SUM(CAST(Churn AS INT)) AS ChurnedCustomers,
    CAST(SUM(CAST(Churn AS INT)) AS FLOAT) / COUNT(*) * 100 AS ChurnRate
FROM [dbo].[customer_churn_dataset-testing-master]
GROUP BY Gender
ORDER BY ChurnRate DESC;

SELECT
    Subscription_Type,
    COUNT(*) AS TotalCustomers,
    SUM(CAST(Churn AS INT)) AS ChurnedCustomers,
    CAST(SUM(CAST(Churn AS INT)) AS FLOAT) / COUNT(*) * 100 AS ChurnRate
FROM [dbo].[customer_churn_dataset-testing-master]
GROUP BY Subscription_Type
ORDER BY ChurnRate DESC;

SELECT
    Contract_Length,
    COUNT(*) AS TotalCustomers,
    SUM(CAST(Churn AS INT)) AS ChurnedCustomers,
    CAST(SUM(CAST(Churn AS INT)) AS FLOAT) / COUNT(*) * 100 AS ChurnRate
FROM [dbo].[customer_churn_dataset-testing-master]
GROUP BY Contract_Length
ORDER BY ChurnRate DESC;

SELECT
    CASE 
        WHEN support_calls <= 2 then 'Low'
        when support_calls <= 5 then 'Medium'
        when support_calls <= 8 then 'High'
        else 'Very High'
    end as SupportCallGroup,
    COUNT(*) as TotalCustomers,
    SUM(CAST(churn as int)) as churnedcustomers,
    CAST(SUM(CAST(churn as int)) as float) / COUNT(*) * 100 as ChurnRate
from [dbo].[customer_churn_dataset-testing-master]
GROUP BY
    case 
          WHEN support_calls <= 2 then 'Low'
        when support_calls <= 5 then 'Medium'
        when support_calls <= 8 then 'High'
        else 'Very High'
    END 
ORDER BY ChurnRate DESC;
