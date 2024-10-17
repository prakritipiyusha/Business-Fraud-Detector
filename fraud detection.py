{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PRE-PROCESSING"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### WRANGLING"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "DATASET LINK (for local machine): https://www.kaggle.com/datasets/chitwanmanchanda/fraudulent-transactions-data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6362620, 11)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read the data\n",
    "df=pd.read_csv('Fraud.csv')\n",
    "# Shape the data\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>type</th>\n",
       "      <th>amount</th>\n",
       "      <th>nameOrig</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>nameDest</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>isFlaggedFraud</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>9839.64</td>\n",
       "      <td>C1231006815</td>\n",
       "      <td>170136.0</td>\n",
       "      <td>160296.36</td>\n",
       "      <td>M1979787155</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>1864.28</td>\n",
       "      <td>C1666544295</td>\n",
       "      <td>21249.0</td>\n",
       "      <td>19384.72</td>\n",
       "      <td>M2044282225</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>181.00</td>\n",
       "      <td>C1305486145</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C553264065</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>181.00</td>\n",
       "      <td>C840083671</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C38997010</td>\n",
       "      <td>21182.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>11668.14</td>\n",
       "      <td>C2048537720</td>\n",
       "      <td>41554.0</td>\n",
       "      <td>29885.86</td>\n",
       "      <td>M1230701703</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>195</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>210370.09</td>\n",
       "      <td>C2121995675</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C1170794006</td>\n",
       "      <td>1442298.03</td>\n",
       "      <td>22190.99</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>196</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>36437.06</td>\n",
       "      <td>C2120063568</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C1740000325</td>\n",
       "      <td>154606.00</td>\n",
       "      <td>1363368.51</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>197</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>82691.56</td>\n",
       "      <td>C1620409359</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C248609774</td>\n",
       "      <td>657983.89</td>\n",
       "      <td>6453430.91</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>198</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>338767.10</td>\n",
       "      <td>C691691381</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C453211571</td>\n",
       "      <td>544481.28</td>\n",
       "      <td>3461666.05</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>199</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>187728.59</td>\n",
       "      <td>C264978436</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C1360767589</td>\n",
       "      <td>394124.51</td>\n",
       "      <td>2107965.39</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>200 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     step      type     amount     nameOrig  oldbalanceOrg  newbalanceOrig  \\\n",
       "0       1   PAYMENT    9839.64  C1231006815       170136.0       160296.36   \n",
       "1       1   PAYMENT    1864.28  C1666544295        21249.0        19384.72   \n",
       "2       1  TRANSFER     181.00  C1305486145          181.0            0.00   \n",
       "3       1  CASH_OUT     181.00   C840083671          181.0            0.00   \n",
       "4       1   PAYMENT   11668.14  C2048537720        41554.0        29885.86   \n",
       "..    ...       ...        ...          ...            ...             ...   \n",
       "195     1  CASH_OUT  210370.09  C2121995675            0.0            0.00   \n",
       "196     1  CASH_OUT   36437.06  C2120063568            0.0            0.00   \n",
       "197     1  CASH_OUT   82691.56  C1620409359            0.0            0.00   \n",
       "198     1  CASH_OUT  338767.10   C691691381            0.0            0.00   \n",
       "199     1  CASH_OUT  187728.59   C264978436            0.0            0.00   \n",
       "\n",
       "        nameDest  oldbalanceDest  newbalanceDest  isFraud  isFlaggedFraud  \n",
       "0    M1979787155            0.00            0.00        0               0  \n",
       "1    M2044282225            0.00            0.00        0               0  \n",
       "2     C553264065            0.00            0.00        1               0  \n",
       "3      C38997010        21182.00            0.00        1               0  \n",
       "4    M1230701703            0.00            0.00        0               0  \n",
       "..           ...             ...             ...      ...             ...  \n",
       "195  C1170794006      1442298.03        22190.99        0               0  \n",
       "196  C1740000325       154606.00      1363368.51        0               0  \n",
       "197   C248609774       657983.89      6453430.91        0               0  \n",
       "198   C453211571       544481.28      3461666.05        0               0  \n",
       "199  C1360767589       394124.51      2107965.39        0               0  \n",
       "\n",
       "[200 rows x 11 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get head of the data\n",
    "df.head(200)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>type</th>\n",
       "      <th>amount</th>\n",
       "      <th>nameOrig</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>nameDest</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>isFlaggedFraud</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6362420</th>\n",
       "      <td>727</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>124582.58</td>\n",
       "      <td>C651444933</td>\n",
       "      <td>124582.58</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C1161818914</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362421</th>\n",
       "      <td>727</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>124582.58</td>\n",
       "      <td>C1098290230</td>\n",
       "      <td>124582.58</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C1739564153</td>\n",
       "      <td>320485.06</td>\n",
       "      <td>445067.64</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362422</th>\n",
       "      <td>727</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>263401.81</td>\n",
       "      <td>C806437930</td>\n",
       "      <td>263401.81</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C1469754483</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362423</th>\n",
       "      <td>727</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>263401.81</td>\n",
       "      <td>C850961884</td>\n",
       "      <td>263401.81</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C1203132980</td>\n",
       "      <td>251586.80</td>\n",
       "      <td>514988.60</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362424</th>\n",
       "      <td>727</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>69039.64</td>\n",
       "      <td>C922622756</td>\n",
       "      <td>69039.64</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C417851521</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362615</th>\n",
       "      <td>743</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>339682.13</td>\n",
       "      <td>C786484425</td>\n",
       "      <td>339682.13</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C776919290</td>\n",
       "      <td>0.00</td>\n",
       "      <td>339682.13</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362616</th>\n",
       "      <td>743</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>6311409.28</td>\n",
       "      <td>C1529008245</td>\n",
       "      <td>6311409.28</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C1881841831</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362617</th>\n",
       "      <td>743</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>6311409.28</td>\n",
       "      <td>C1162922333</td>\n",
       "      <td>6311409.28</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C1365125890</td>\n",
       "      <td>68488.84</td>\n",
       "      <td>6379898.11</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362618</th>\n",
       "      <td>743</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>850002.52</td>\n",
       "      <td>C1685995037</td>\n",
       "      <td>850002.52</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C2080388513</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6362619</th>\n",
       "      <td>743</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>850002.52</td>\n",
       "      <td>C1280323807</td>\n",
       "      <td>850002.52</td>\n",
       "      <td>0.0</td>\n",
       "      <td>C873221189</td>\n",
       "      <td>6510099.11</td>\n",
       "      <td>7360101.63</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>200 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         step      type      amount     nameOrig  oldbalanceOrg  \\\n",
       "6362420   727  TRANSFER   124582.58   C651444933      124582.58   \n",
       "6362421   727  CASH_OUT   124582.58  C1098290230      124582.58   \n",
       "6362422   727  TRANSFER   263401.81   C806437930      263401.81   \n",
       "6362423   727  CASH_OUT   263401.81   C850961884      263401.81   \n",
       "6362424   727  TRANSFER    69039.64   C922622756       69039.64   \n",
       "...       ...       ...         ...          ...            ...   \n",
       "6362615   743  CASH_OUT   339682.13   C786484425      339682.13   \n",
       "6362616   743  TRANSFER  6311409.28  C1529008245     6311409.28   \n",
       "6362617   743  CASH_OUT  6311409.28  C1162922333     6311409.28   \n",
       "6362618   743  TRANSFER   850002.52  C1685995037      850002.52   \n",
       "6362619   743  CASH_OUT   850002.52  C1280323807      850002.52   \n",
       "\n",
       "         newbalanceOrig     nameDest  oldbalanceDest  newbalanceDest  isFraud  \\\n",
       "6362420             0.0  C1161818914            0.00            0.00        1   \n",
       "6362421             0.0  C1739564153       320485.06       445067.64        1   \n",
       "6362422             0.0  C1469754483            0.00            0.00        1   \n",
       "6362423             0.0  C1203132980       251586.80       514988.60        1   \n",
       "6362424             0.0   C417851521            0.00            0.00        1   \n",
       "...                 ...          ...             ...             ...      ...   \n",
       "6362615             0.0   C776919290            0.00       339682.13        1   \n",
       "6362616             0.0  C1881841831            0.00            0.00        1   \n",
       "6362617             0.0  C1365125890        68488.84      6379898.11        1   \n",
       "6362618             0.0  C2080388513            0.00            0.00        1   \n",
       "6362619             0.0   C873221189      6510099.11      7360101.63        1   \n",
       "\n",
       "         isFlaggedFraud  \n",
       "6362420               0  \n",
       "6362421               0  \n",
       "6362422               0  \n",
       "6362423               0  \n",
       "6362424               0  \n",
       "...                 ...  \n",
       "6362615               0  \n",
       "6362616               0  \n",
       "6362617               0  \n",
       "6362618               0  \n",
       "6362619               0  \n",
       "\n",
       "[200 rows x 11 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(200)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### ANALYSIS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check for null values\n",
    "df.isnull().values.any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 6362620 entries, 0 to 6362619\n",
      "Data columns (total 11 columns):\n",
      " #   Column          Dtype  \n",
      "---  ------          -----  \n",
      " 0   step            int64  \n",
      " 1   type            object \n",
      " 2   amount          float64\n",
      " 3   nameOrig        object \n",
      " 4   oldbalanceOrg   float64\n",
      " 5   newbalanceOrig  float64\n",
      " 6   nameDest        object \n",
      " 7   oldbalanceDest  float64\n",
      " 8   newbalanceDest  float64\n",
      " 9   isFraud         int64  \n",
      " 10  isFlaggedFraud  int64  \n",
      "dtypes: float64(5), int64(3), object(3)\n",
      "memory usage: 534.0+ MB\n"
     ]
    }
   ],
   "source": [
    "# Getting information about data\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is a really big dataset with no NULL values having size over 500MB. This would take some time to train for a normal GPU."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Legit transactions:  6354407\n",
      "Number of Fraud transactions:  8213\n",
      "Percentage of Legit transactions: 99.8709 %\n",
      "Percentage of Fraud transactions: 0.1291 %\n"
     ]
    }
   ],
   "source": [
    "legit = len(df[df.isFraud == 0])\n",
    "fraud = len(df[df.isFraud == 1])\n",
    "legit_percent = (legit / (fraud + legit)) * 100\n",
    "fraud_percent = (fraud / (fraud + legit)) * 100\n",
    "\n",
    "print(\"Number of Legit transactions: \", legit)\n",
    "print(\"Number of Fraud transactions: \", fraud)\n",
    "print(\"Percentage of Legit transactions: {:.4f} %\".format(legit_percent))\n",
    "print(\"Percentage of Fraud transactions: {:.4f} %\".format(fraud_percent))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "These results prove that this is a highly unbalanced data as Percentage of Legit transactions= 99.87 % and Percentage of Fraud transactions= 0.13 %. \n",
    "SO DECISION TREES AND RANDOM FORESTS ARE GOOD METHODS FOR IMBALANCED DATA."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>type</th>\n",
       "      <th>amount</th>\n",
       "      <th>nameOrig</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>nameDest</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>isFlaggedFraud</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>9839.64</td>\n",
       "      <td>C1231006815</td>\n",
       "      <td>170136.0</td>\n",
       "      <td>160296.36</td>\n",
       "      <td>M1979787155</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>1864.28</td>\n",
       "      <td>C1666544295</td>\n",
       "      <td>21249.0</td>\n",
       "      <td>19384.72</td>\n",
       "      <td>M2044282225</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>11668.14</td>\n",
       "      <td>C2048537720</td>\n",
       "      <td>41554.0</td>\n",
       "      <td>29885.86</td>\n",
       "      <td>M1230701703</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>7817.71</td>\n",
       "      <td>C90045638</td>\n",
       "      <td>53860.0</td>\n",
       "      <td>46042.29</td>\n",
       "      <td>M573487274</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>7107.77</td>\n",
       "      <td>C154988899</td>\n",
       "      <td>183195.0</td>\n",
       "      <td>176087.23</td>\n",
       "      <td>M408069119</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   step     type    amount     nameOrig  oldbalanceOrg  newbalanceOrig  \\\n",
       "0     1  PAYMENT   9839.64  C1231006815       170136.0       160296.36   \n",
       "1     1  PAYMENT   1864.28  C1666544295        21249.0        19384.72   \n",
       "4     1  PAYMENT  11668.14  C2048537720        41554.0        29885.86   \n",
       "5     1  PAYMENT   7817.71    C90045638        53860.0        46042.29   \n",
       "6     1  PAYMENT   7107.77   C154988899       183195.0       176087.23   \n",
       "\n",
       "      nameDest  oldbalanceDest  newbalanceDest  isFraud  isFlaggedFraud  \n",
       "0  M1979787155             0.0             0.0        0               0  \n",
       "1  M2044282225             0.0             0.0        0               0  \n",
       "4  M1230701703             0.0             0.0        0               0  \n",
       "5   M573487274             0.0             0.0        0               0  \n",
       "6   M408069119             0.0             0.0        0               0  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Merchants\n",
    "X = df[df['nameDest'].str.contains('M')]\n",
    "X.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For merchants there is no information regarding the attribites oldbalanceDest and newbalanceDest. This is because "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## VISUALISATION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### CORRELATION HEATMAP"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x432 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "corr=df.corr()\n",
    "\n",
    "plt.figure(figsize=(10,6))\n",
    "sns.heatmap(corr,annot=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### NUMBER OF LEGIT AND FRAUD TRANSACTIONS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAUAAAAJcCAYAAACIbH3XAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAZu0lEQVR4nO3debCldX3n8fcHGgVk0/QdCkVp4xaVRNQWR9yXpDCa0UkQQY1LTKgxM5TGUQdHw8SUmUqq1AqJ27QMIuOuEUclAU0CEhJBuhWUzRkHm4CoNChrXAJ854/ztFwul+5zu/s59zbf96vqVp/znHOe3+8u/b7Pcs65qSokqaNdlnsCkrRcDKCktgygpLYMoKS2DKCktgygpLYM4D1MkouTPGPkMSrJQ4fL70/yhyOM8TdJXrGj1zvFuG9Pcm2S7+/Ada4ZvmarZvlYbV18HuDOI8npwFer6vgFy18A/A/gwKq6dQbzKOBhVfXtHbS+PwIeWlUv2xHr2455PAj4FnBQVV2zyO3PAD5cVQcucb1rgO8Auy31+7M9j9XWuQW4c/kQ8LIkWbD8t4GP+B9kuz0IuG6x+OmeyQDuXD4L/ALw1M0LktwXeD5wynB9Y5LnDJcPTbI+yY1JfpDkXcPyZyS5av6KF3ncV5Jcn+R7Sd6d5F6LTSjJyUnePlz+fJKb533cnuSVw20nJLlymMuGJE8dlh8O/FfgxcNjLhyWn5Xkd4fLuyR5a5IrklyT5JQk+w63bd5FfEWSfx52X99yd1/AJPsOj980rO+tw/qfA3wJuP8wj5OX8H0hyfOSfH34/K4ctmoX+p0kVw9f0zfMe+wuSY5L8v+SXJfkk0nudzfjvDLJ5UluSvKdJC9dyjx1ZwZwJ1JVPwY+Cbx83uIjgcuq6sJFHnICcEJV7QM8ZHjsNG4D/gBYDTwJeDbw+1PM7zeqaq+q2gt4EfB94O+Gm88HDgHuB3wU+FSS3avqdOC/A58YHvuYRVb9yuHjmcAvAnsB715wn6cAjxjmenySR97NNP8S2HdYz9OZfC1fVVV/CzwXuHqYxyu39vkucMuwrv2A5wGvSfLCBfd5JvAw4NeA/7L5Fw5wLPDCYT73B34EvGfhAEnuA/wF8Nyq2hs4DLhgifPUPCsugElOGn7LXzTl/Y9Mcslw8P+jY89vBfgQcESS3YfrLx+WLeZfgYcmWV1VN1fVudMMUFUbqurcqrq1qjYyOb749GknmOThw5yOrKorh3V+uKquG9b5TuDeTII1jZcC76qqy6vqZuDNwFELTgy8rap+PPwiuBC4S0iT7AocBby5qm4aPrd3MjmEsF2q6qyq+mZV3V5V3wA+xl2/Zm+rqluq6pvAB4Gjh+X/AXhLVV1VVT8F/ojJ93ixEx+3Awcn2aOqvldVF2/v3DtbcQEETgYOn+aOSR7G5D/Dk6vq0cDrxpvWylBV5wDXAi9M8hDgUCZbVIt5NfBw4LIk5yd5/jRjJHl4ki8k+X6SG5lsoa2e8rH7Av8beOsw183L35Dk0iQ3JLmeyVbYVOtkslV0xbzrVwCrgP3nLZt/1vZfmGwlLrQa2G2RdT1gynncrSRPTHLmsGt9A5OoLfz8rlww7v2HywcBpw6HHK4HLmWyFT7/86OqbgFePKz7e0lOS/JL2zv3zlZcAKvqbOCH85cleUiS04djR/8w75v+e8B7qupHw2O7HLw+hcmW38uAM6rqB4vdqar+b1UdDfwb4M+ATw+7UbcAe26+37BlNDfvoe8DLmNypncfJsfoFp54uYskuzCJ8ZlVtW7e8qcCb2Kyu37fqtoPuGHeOrf2VISrmURiswcBtwKLft5bcC2TreKF6/ruEtezmI8CnwMeWFX7Au/nrl+zBy4Y9+rh8pVMdmv3m/exe1XdZV5VdUZV/SpwAJPv0Qd2wNzbWnEBvBvrgGOr6vHAG4D3DssfDjw8yT8mOXc4oN7BKcBzmPwCuLvdX5K8LMlcVd0OXD8svh34P8Duw4H73YC3Mtkl3Wxv4Ebg5uGXzWumnNefAPcBXrtg+d5MgrUJWJXkeGCfebf/AFgzBHQxHwP+IMmDk+zFHccMl3TWu6puY3Ic9E+S7J3kIOD1wIeXsp4kuy/4yPA5/rCqfpLkUOAlizz0D5PsmeTRwKuATwzL3z/M6aBh/XOZPLVp4bj7J3nB8Evsp8DNTL6f2kYrPoDDD/xhTA6aX8DkeNQBw82rmBxUfgaT4ykfSLLf7Gc5W8Oxq39iEpvPbeGuhwMXJ7mZyQmRo4bjZDcwOalxIpOtn1uA+WeF38DkP/BNTLYwPsF0jgb+LfCj3HEm+KXAGcDpTMJ7BfAT7rw7+Knh3+uSfG2R9Z4E/C/gbCbPifsJkxMH2+JYJp/v5cA5TLbcTlrC4x8A/HjBx0OYfD3/OMlNwPEsfsLpy8C3mZwYekdVfXFYfgKT7+MXh8efCzxxkcfvwiTYVzPZS3o60/9y0iJW5BOhM3ny5xeq6uAk+wDfqqoDFrnf+4HzquqDw/W/A46rqvNnOmFJO6UVvwVYVTcC30nyIoBMbD7D91kmW38kWc1kl/jyZZimpJ3Qigtgko8BXwEekeSqJK9m8jSIV2fyJNmLgc3HR85gstt0CXAm8Maqum455i1p57Mid4ElaRZW3BagJM3KinqLndWrV9eaNWuWexqS7mE2bNhwbVXNLVy+ogK4Zs0a1q9fv9zTkHQPk+SKxZa7CyypLQMoqS0DKKktAyipLQMoqS0DKKktAyipLQMoqS0DKKktAyipLQMoqS0DKKktAyipLQMoqS0DKKktAyipLQMoqS0DKKktAyipLQMoqS0DKKktAyipLQMoqS0DKKmtFfWH0VeKNcedttxTWJE2/unzlnsK0g7lFqCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktkYNYJL9knw6yWVJLk3ypDHHk6SlWDXy+k8ATq+qI5LcC9hz5PEkaWqjBTDJvsDTgFcCVNXPgJ+NNZ4kLdWYu8APBjYBH0zy9SQnJrnPwjslOSbJ+iTrN23aNOJ0JOnOxgzgKuBxwPuq6rHALcBxC+9UVeuqam1VrZ2bmxtxOpJ0Z2MG8Crgqqo6b7j+aSZBlKQVYbQAVtX3gSuTPGJY9GzgkrHGk6SlGvss8LHAR4YzwJcDrxp5PEma2qgBrKoLgLVjjiFJ28pXgkhqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmrLAEpqywBKassASmpr1ZgrT7IRuAm4Dbi1qtaOOZ4kLcWoARw8s6quncE4krQk7gJLamvsABbwxSQbkhyz2B2SHJNkfZL1mzZtGnk6knSHsQP4lKp6HPBc4D8medrCO1TVuqpaW1Vr5+bmRp6OJN1h1ABW1XeHf68BTgUOHXM8SVqK0QKY5D5J9t58Gfg14KKxxpOkpRrzLPD+wKlJNo/z0ao6fcTxJGlJRgtgVV0OPGas9UvS9vJpMJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaMoCS2jKAktoygJLaGj2ASXZN8vUkXxh7LElaillsAb4WuHQG40jSkowawCQHAs8DThxzHEnaFmNvAf458Cbg9ru7Q5JjkqxPsn7Tpk0jT0eS7jBaAJM8H7imqjZs6X5Vta6q1lbV2rm5ubGmI0l3MeYW4JOBf5dkI/Bx4FlJPjzieJK0JKMFsKreXFUHVtUa4Cjg76vqZWONJ0lL5fMAJbW1ahaDVNVZwFmzGEuSpuUWoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLYMoKS2DKCktgygpLamCmCSJ0+zTJJ2JtNuAf7llMskaaexaks3JnkScBgwl+T1827aB9h1zIlJ0ti2GEDgXsBew/32nrf8RuCIsSYlSbOwxQBW1ZeBLyc5uaqumNGcJGkm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",
      "text/plain": [
       "<Figure size 360x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(5,10))\n",
    "labels = [\"Legit\", \"Fraud\"]\n",
    "count_classes = df.value_counts(df['isFraud'], sort= True)\n",
    "count_classes.plot(kind = \"bar\", rot = 0)\n",
    "plt.title(\"Visualization of Labels\")\n",
    "plt.ylabel(\"Count\")\n",
    "plt.xticks(range(2), labels)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PROBLEM SOLVING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>type</th>\n",
       "      <th>amount</th>\n",
       "      <th>nameOrig</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>nameDest</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>isFlaggedFraud</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>9839.64</td>\n",
       "      <td>C1231006815</td>\n",
       "      <td>170136.0</td>\n",
       "      <td>160296.36</td>\n",
       "      <td>M1979787155</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>1864.28</td>\n",
       "      <td>C1666544295</td>\n",
       "      <td>21249.0</td>\n",
       "      <td>19384.72</td>\n",
       "      <td>M2044282225</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>TRANSFER</td>\n",
       "      <td>181.00</td>\n",
       "      <td>C1305486145</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C553264065</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>CASH_OUT</td>\n",
       "      <td>181.00</td>\n",
       "      <td>C840083671</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>C38997010</td>\n",
       "      <td>21182.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>PAYMENT</td>\n",
       "      <td>11668.14</td>\n",
       "      <td>C2048537720</td>\n",
       "      <td>41554.0</td>\n",
       "      <td>29885.86</td>\n",
       "      <td>M1230701703</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   step      type    amount     nameOrig  oldbalanceOrg  newbalanceOrig  \\\n",
       "0     1   PAYMENT   9839.64  C1231006815       170136.0       160296.36   \n",
       "1     1   PAYMENT   1864.28  C1666544295        21249.0        19384.72   \n",
       "2     1  TRANSFER    181.00  C1305486145          181.0            0.00   \n",
       "3     1  CASH_OUT    181.00   C840083671          181.0            0.00   \n",
       "4     1   PAYMENT  11668.14  C2048537720        41554.0        29885.86   \n",
       "\n",
       "      nameDest  oldbalanceDest  newbalanceDest  isFraud  isFlaggedFraud  \n",
       "0  M1979787155             0.0             0.0        0               0  \n",
       "1  M2044282225             0.0             0.0        0               0  \n",
       "2   C553264065             0.0             0.0        1               0  \n",
       "3    C38997010         21182.0             0.0        1               0  \n",
       "4  M1230701703             0.0             0.0        0               0  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#creating a copy of original dataset to train and test models\n",
    "\n",
    "new_df=df.copy()\n",
    "new_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### LABEL ENCODING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['type', 'nameOrig', 'nameDest'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Checking how many attributes are dtype: object\n",
    "\n",
    "objList = new_df.select_dtypes(include = \"object\").columns\n",
    "print (objList)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "THERE ARE 3 ATTRIBUTES WITH Object Datatype. THUS WE NEED TO LABEL ENCODE THEM IN ORDER TO CHECK MULTICOLINEARITY."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 6362620 entries, 0 to 6362619\n",
      "Data columns (total 11 columns):\n",
      " #   Column          Dtype  \n",
      "---  ------          -----  \n",
      " 0   step            int64  \n",
      " 1   type            int32  \n",
      " 2   amount          float64\n",
      " 3   nameOrig        int32  \n",
      " 4   oldbalanceOrg   float64\n",
      " 5   newbalanceOrig  float64\n",
      " 6   nameDest        int32  \n",
      " 7   oldbalanceDest  float64\n",
      " 8   newbalanceDest  float64\n",
      " 9   isFraud         int64  \n",
      " 10  isFlaggedFraud  int64  \n",
      "dtypes: float64(5), int32(3), int64(3)\n",
      "memory usage: 461.2 MB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "#Label Encoding for object to numeric conversion\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "le = LabelEncoder()\n",
    "\n",
    "for feat in objList:\n",
    "    new_df[feat] = le.fit_transform(new_df[feat].astype(str))\n",
    "\n",
    "print (new_df.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>step</th>\n",
       "      <th>type</th>\n",
       "      <th>amount</th>\n",
       "      <th>nameOrig</th>\n",
       "      <th>oldbalanceOrg</th>\n",
       "      <th>newbalanceOrig</th>\n",
       "      <th>nameDest</th>\n",
       "      <th>oldbalanceDest</th>\n",
       "      <th>newbalanceDest</th>\n",
       "      <th>isFraud</th>\n",
       "      <th>isFlaggedFraud</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>9839.64</td>\n",
       "      <td>757869</td>\n",
       "      <td>170136.0</td>\n",
       "      <td>160296.36</td>\n",
       "      <td>1662094</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1864.28</td>\n",
       "      <td>2188998</td>\n",
       "      <td>21249.0</td>\n",
       "      <td>19384.72</td>\n",
       "      <td>1733924</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>181.00</td>\n",
       "      <td>1002156</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>439685</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>181.00</td>\n",
       "      <td>5828262</td>\n",
       "      <td>181.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>391696</td>\n",
       "      <td>21182.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>11668.14</td>\n",
       "      <td>3445981</td>\n",
       "      <td>41554.0</td>\n",
       "      <td>29885.86</td>\n",
       "      <td>828919</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   step  type    amount  nameOrig  oldbalanceOrg  newbalanceOrig  nameDest  \\\n",
       "0     1     3   9839.64    757869       170136.0       160296.36   1662094   \n",
       "1     1     3   1864.28   2188998        21249.0        19384.72   1733924   \n",
       "2     1     4    181.00   1002156          181.0            0.00    439685   \n",
       "3     1     1    181.00   5828262          181.0            0.00    391696   \n",
       "4     1     3  11668.14   3445981        41554.0        29885.86    828919   \n",
       "\n",
       "   oldbalanceDest  newbalanceDest  isFraud  isFlaggedFraud  \n",
       "0             0.0             0.0        0               0  \n",
       "1             0.0             0.0        0               0  \n",
       "2             0.0             0.0        1               0  \n",
       "3         21182.0             0.0        1               0  \n",
       "4             0.0             0.0        0               0  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### MULTICOLINEARITY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>variables</th>\n",
       "      <th>VIF</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>step</td>\n",
       "      <td>2.791610</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>type</td>\n",
       "      <td>4.467405</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>amount</td>\n",
       "      <td>4.149312</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>nameOrig</td>\n",
       "      <td>2.764234</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>oldbalanceOrg</td>\n",
       "      <td>576.803777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>newbalanceOrig</td>\n",
       "      <td>582.709128</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>nameDest</td>\n",
       "      <td>3.300975</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>oldbalanceDest</td>\n",
       "      <td>73.349937</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>newbalanceDest</td>\n",
       "      <td>85.005614</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>isFraud</td>\n",
       "      <td>1.195305</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>isFlaggedFraud</td>\n",
       "      <td>1.002587</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         variables         VIF\n",
       "0             step    2.791610\n",
       "1             type    4.467405\n",
       "2           amount    4.149312\n",
       "3         nameOrig    2.764234\n",
       "4    oldbalanceOrg  576.803777\n",
       "5   newbalanceOrig  582.709128\n",
       "6         nameDest    3.300975\n",
       "7   oldbalanceDest   73.349937\n",
       "8   newbalanceDest   85.005614\n",
       "9          isFraud    1.195305\n",
       "10  isFlaggedFraud    1.002587"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import library for VIF (VARIANCE INFLATION FACTOR)\n",
    "\n",
    "from statsmodels.stats.outliers_influence import variance_inflation_factor\n",
    "\n",
    "def calc_vif(df):\n",
    "\n",
    "    # Calculating VIF\n",
    "    vif = pd.DataFrame()\n",
    "    vif[\"variables\"] = df.columns\n",
    "    vif[\"VIF\"] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]\n",
    "\n",
    "    return(vif)\n",
    "\n",
    "calc_vif(new_df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see that oldbalanceOrg and newbalanceOrig have too high VIF thus they are highly correlated. Similarly oldbalanceDest and newbalanceDest. Also nameDest is connected to nameOrig.\n",
    "\n",
    "Thus combine these pairs of collinear attributes and drop the individual ones."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>variables</th>\n",
       "      <th>VIF</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>type</td>\n",
       "      <td>2.687803</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>amount</td>\n",
       "      <td>3.818902</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>isFraud</td>\n",
       "      <td>1.184479</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>isFlaggedFraud</td>\n",
       "      <td>1.002546</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Actual_amount_orig</td>\n",
       "      <td>1.307910</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Actual_amount_dest</td>\n",
       "      <td>3.754335</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>TransactionPath</td>\n",
       "      <td>2.677167</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            variables       VIF\n",
       "0                type  2.687803\n",
       "1              amount  3.818902\n",
       "2             isFraud  1.184479\n",
       "3      isFlaggedFraud  1.002546\n",
       "4  Actual_amount_orig  1.307910\n",
       "5  Actual_amount_dest  3.754335\n",
       "6     TransactionPath  2.677167"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['Actual_amount_orig'] = new_df.apply(lambda x: x['oldbalanceOrg'] - x['newbalanceOrig'],axis=1)\n",
    "new_df['Actual_amount_dest'] = new_df.apply(lambda x: x['oldbalanceDest'] - x['newbalanceDest'],axis=1)\n",
    "new_df['TransactionPath'] = new_df.apply(lambda x: x['nameOrig'] + x['nameDest'],axis=1)\n",
    "\n",
    "#Dropping columns\n",
    "new_df = new_df.drop(['oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest','step','nameOrig','nameDest'],axis=1)\n",
    "\n",
    "calc_vif(new_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x432 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "corr=new_df.corr()\n",
    "\n",
    "plt.figure(figsize=(10,6))\n",
    "sns.heatmap(corr,annot=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br>How did you select variables to be included in the model?\n",
    "<br>Using the VIF values and correlation heatmap. We just need to check if there are any two attributes highly correlated to each other and then drop the one which is less correlated to the isFraud Attribute."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## MODEL BUILDING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "import itertools\n",
    "from collections import Counter\n",
    "import sklearn.metrics as metrics\n",
    "from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### NORMALIZING (SCALING) AMOUNT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform Scaling\n",
    "scaler = StandardScaler()\n",
    "new_df[\"NormalizedAmount\"] = scaler.fit_transform(new_df[\"amount\"].values.reshape(-1, 1))\n",
    "new_df.drop([\"amount\"], inplace= True, axis= 1)\n",
    "\n",
    "Y = new_df[\"isFraud\"]\n",
    "X = new_df.drop([\"isFraud\"], axis= 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I did not normalize the complete dataset because it may lead to decrease in accuracy of model."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### TRAIN-TEST SPLIT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape of X_train:  (4453834, 6)\n",
      "Shape of X_test:  (1908786, 6)\n"
     ]
    }
   ],
   "source": [
    "# Split the data\n",
    "(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size= 0.3, random_state= 42)\n",
    "\n",
    "print(\"Shape of X_train: \", X_train.shape)\n",
    "print(\"Shape of X_test: \", X_test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### MODEL TRAINIG"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# DECISION TREE\n",
    "\n",
    "decision_tree = DecisionTreeClassifier()\n",
    "decision_tree.fit(X_train, Y_train)\n",
    "\n",
    "Y_pred_dt = decision_tree.predict(X_test)\n",
    "decision_tree_score = decision_tree.score(X_test, Y_test) * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# RANDOM FOREST\n",
    "\n",
    "random_forest = RandomForestClassifier(n_estimators= 100)\n",
    "random_forest.fit(X_train, Y_train)\n",
    "\n",
    "Y_pred_rf = random_forest.predict(X_test)\n",
    "random_forest_score = random_forest.score(X_test, Y_test) * 100"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### EVALUATION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Decision Tree Score:  99.92277814275671\n",
      "Random Forest Score:  99.95871721607347\n"
     ]
    }
   ],
   "source": [
    "# Print scores of our classifiers\n",
    "\n",
    "print(\"Decision Tree Score: \", decision_tree_score)\n",
    "print(\"Random Forest Score: \", random_forest_score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TP,FP,TN,FN - Decision Tree\n",
      "True Positives: 1714\n",
      "False Positives: 753\n",
      "True Negatives: 1905598\n",
      "False Negatives: 721\n",
      "----------------------------------------------------------------------------------------\n",
      "TP,FP,TN,FN - Random Forest\n",
      "True Positives: 1712\n",
      "False Positives: 65\n",
      "True Negatives: 1906286\n",
      "False Negatives: 723\n"
     ]
    }
   ],
   "source": [
    "# key terms of Confusion Matrix - DT\n",
    "\n",
    "print(\"TP,FP,TN,FN - Decision Tree\")\n",
    "tn, fp, fn, tp = confusion_matrix(Y_test, Y_pred_dt).ravel()\n",
    "print(f'True Positives: {tp}')\n",
    "print(f'False Positives: {fp}')\n",
    "print(f'True Negatives: {tn}')\n",
    "print(f'False Negatives: {fn}')\n",
    "\n",
    "print(\"----------------------------------------------------------------------------------------\")\n",
    "\n",
    "# key terms of Confusion Matrix - RF\n",
    "\n",
    "print(\"TP,FP,TN,FN - Random Forest\")\n",
    "tn, fp, fn, tp = confusion_matrix(Y_test, Y_pred_rf).ravel()\n",
    "print(f'True Positives: {tp}')\n",
    "print(f'False Positives: {fp}')\n",
    "print(f'True Negatives: {tn}')\n",
    "print(f'False Negatives: {fn}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br>TP(Decision Tree) ~ TP(Random Forest) so no competetion here.\n",
    "<br>FP(Decision Tree) >> FP(Random Forest) - Random Forest has an edge\n",
    "<br>TN(Decision Tree) < TN(Random Forest) - Random Forest is better here too\n",
    "<br>FN(Decision Tree) ~ FN(Random Forest)\n",
    "\n",
    "<br> Here Random Forest looks good."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Confusion Matrix - Decision Tree\n",
      "[[1905598     753]\n",
      " [    721    1714]]\n",
      "----------------------------------------------------------------------------------------\n",
      "Confusion Matrix - Random Forest\n",
      "[[1906286      65]\n",
      " [    723    1712]]\n"
     ]
    }
   ],
   "source": [
    "# confusion matrix - DT\n",
    "\n",
    "confusion_matrix_dt = confusion_matrix(Y_test, Y_pred_dt.round())\n",
    "print(\"Confusion Matrix - Decision Tree\")\n",
    "print(confusion_matrix_dt,)\n",
    "\n",
    "print(\"----------------------------------------------------------------------------------------\")\n",
    "\n",
    "# confusion matrix - RF\n",
    "\n",
    "confusion_matrix_rf = confusion_matrix(Y_test, Y_pred_rf.round())\n",
    "print(\"Confusion Matrix - Random Forest\")\n",
    "print(confusion_matrix_rf)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report - Decision Tree\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      1.00      1.00   1906351\n",
      "           1       0.69      0.70      0.70      2435\n",
      "\n",
      "    accuracy                           1.00   1908786\n",
      "   macro avg       0.85      0.85      0.85   1908786\n",
      "weighted avg       1.00      1.00      1.00   1908786\n",
      "\n",
      "----------------------------------------------------------------------------------------\n",
      "Classification Report - Random Forest\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      1.00      1.00   1906351\n",
      "           1       0.96      0.70      0.81      2435\n",
      "\n",
      "    accuracy                           1.00   1908786\n",
      "   macro avg       0.98      0.85      0.91   1908786\n",
      "weighted avg       1.00      1.00      1.00   1908786\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# classification report - DT\n",
    "\n",
    "classification_report_dt = classification_report(Y_test, Y_pred_dt)\n",
    "print(\"Classification Report - Decision Tree\")\n",
    "print(classification_report_dt)\n",
    "\n",
    "print(\"----------------------------------------------------------------------------------------\")\n",
    "\n",
    "# classification report - RF\n",
    "\n",
    "classification_report_rf = classification_report(Y_test, Y_pred_rf)\n",
    "print(\"Classification Report - Random Forest\")\n",
    "print(classification_report_rf)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "With Such a good precision and hence F1-Score, Random Forest comes out to be better as expected."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# visualising confusion matrix - DT\n",
    "\n",
    "\n",
    "disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_dt)\n",
    "disp.plot()\n",
    "plt.title('Confusion Matrix - DT')\n",
    "plt.show()\n",
    "\n",
    "# visualising confusion matrix - RF\n",
    "disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_rf)\n",
    "disp.plot()\n",
    "plt.title('Confusion Matrix - RF')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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n6FDh/587qyzzmLKlClMmTKFQYMGVSqeZKnrCeDbb+HKK+HZZ8Og9fXXh/pMKuInUmWuuSYsO6pKHTrAn/6U+JrVq1fz/vvv8+6773LyySdz++23l/u+a9as4dFHH2X+/PnUrl0bgD322IO+fftWKt6XXnqJfv36Ubt2bZo1a0bz5s35+OOP6d69+2bXmRk//vgjACtXrmTvDE/BL+yfhO7wxBPhO3j1avjf/4UbbghdTiKSF1566SV69uxJy5YtadCgARMnTqRz584Jv2bu3Lk0adKEHZPocr722mt59913t3i9X79+3HzzzZu9tnjxYg466KCfjxs1asTixYu3+NoRI0Zw4oknUrduXXbccUfGjx//87nnn3+ecePG0bJlS+677z4aN25cboyVVdiJYsECGDQIunQJq6tbtcp0RCJ5q7zf/FNl9OjRXH311UD44T169Gg6d+681dlB2zpr6L777qt0jGW956uvvkq3bt246667uO666xgxYgQnn3wyZ599NrVr1+aRRx7h/PPP55133qnyzy+t8BJFSRG/E04IRfw++CBUe1V9JpG888MPP/DOO+8wffp0zIzi4mLMjLvuuosGDRqwfPnyLa7fddddad68OQsWLODHH38st1WxLS2Khg0bsnDhwp+PFy1aRMOGDTe7ZunSpUydOpVu3boBYUyiZ8+eADRo0ODn6wYNGsSNN96YxF2oAu6eU486dTp7hc2Z437ooe7gPnZsxd9HRJIya9asjH7+I4884oMHD97stcMOO8zfe+89Lyoq8qZNm/4c45dffulNmjTxFStWuLv7DTfc4AMGDPB169a5u/t3333nzzzzTKXimTFjhrdr186Liop83rx53qxZM9+4ceNm12zYsMEbNGjgc+bMcXf3ESNG+Omnn+7u7l9//fXP173wwgverVu3Mj+nrPsOTPAK/twtjBbFxo1wzz1w661Qty789a+azSRSAEaPHs1NN9202Wt9+vRh9OjRHHbYYTzxxBMMHDiQoqIiatasyYgRI6hfvz4AQ4cO5ZZbbqFNmzbUqVOHevXqMWTIkErFc8ABB9C3b1/atGlDjRo1GDZsGNWj3owTTzyRESNGsPfee/Poo4/Sp08fqlWrxs4778zIkSMBuP/++xkzZgw1atRgl112YdSoUZWKJ1mFUevp+OPhzTfh9NPDmog990xNcCKy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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# AUC ROC - DT\n",
    "# calculate the fpr and tpr for all thresholds of the classification\n",
    "\n",
    "fpr, tpr, threshold = metrics.roc_curve(Y_test, Y_pred_dt)\n",
    "roc_auc = metrics.auc(fpr, tpr)\n",
    "\n",
    "plt.title('ROC - DT')\n",
    "plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)\n",
    "plt.legend(loc = 'lower right')\n",
    "plt.plot([0, 1], [0, 1],'r--')\n",
    "plt.xlim([0, 1])\n",
    "plt.ylim([0, 1])\n",
    "plt.ylabel('True Positive Rate')\n",
    "plt.xlabel('False Positive Rate')\n",
    "plt.show()\n",
    "\n",
    "# AUC ROC - RF\n",
    "# calculate the fpr and tpr for all thresholds of the classification\n",
    "\n",
    "fpr, tpr, threshold = metrics.roc_curve(Y_test, Y_pred_rf)\n",
    "roc_auc = metrics.auc(fpr, tpr)\n",
    "\n",
    "plt.title('ROC - RF')\n",
    "plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)\n",
    "plt.legend(loc = 'lower right')\n",
    "plt.plot([0, 1], [0, 1],'r--')\n",
    "plt.xlim([0, 1])\n",
    "plt.ylim([0, 1])\n",
    "plt.ylabel('True Positive Rate')\n",
    "plt.xlabel('False Positive Rate')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "THE AUC for both Decision Tree and Random Forest is equal, so both models are pretty good at what they do."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## CONCLUSION"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br>We have seen that Accuracy of both Random Forest and Decision Tree is equal, although teh precision of Random Forest is more. In a fraud detection model, Precision is highly important because rather than predicting normal transactions correctly we want Fraud transactions to be predicted correctly and Legit to be left off.If either of the 2 reasons are not fulfiiled we may catch the innocent and leave the culprit.\n",
    "<br>This is also one of the reason why Random Forest and Decision Tree are used unstead of other algorithms.\n",
    "\n",
    "<br>Also the reason I have chosen this model is because of highly unbalanced dataset (Legit: Fraud :: 99.87:0.13). Random forest makes multiple decision trees which makes it easier (although time taking) for model to understand the data in a simpler way since Decision Tree makes decisions in a boolean way.\n",
    "\n",
    "<br>Models like XGBoost, Bagging, ANN, and Logistic Regression may give good accuracy but they won't give good precision and recall values."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the key factors that predict fraudulent customer?\n",
    "1. The source of request is secured or not ?\n",
    "2. Is the name of organisation asking for money is legit or not ?\n",
    "3. Transaction history of vendors."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What kind of prevention should be adopted while company update its infrastructure?\n",
    "1. Use smart vertified apps only.\n",
    "2. Browse through secured websites.\n",
    "3. Use secured internet connections (USE VPN).\n",
    "4. Keep your mobile and laptop security updated.\n",
    "5. Don't respond to unsolicited calls/SMS(s/E-mails.\n",
    "6. If you feel like you have been tricked or security compromised, contact your bank immidiately."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assuming these actions have been implemented, how would you determine if they work?\n",
    "1. Bank sending E-statements.\n",
    "2. Customers keeping a check of their account activity.\n",
    "4. Always keep a log of your payments."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.6 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "9f1ed5a6caa63b933f18b2de58eb1658054e234b84bf4970be74ffb1abce9f96"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
