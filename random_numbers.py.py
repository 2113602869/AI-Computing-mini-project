{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5d63c80c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "随机数已成功写入到 data.txt 文件中！\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "# 生成100000个随机数\n",
    "random_numbers = [random.randint(1, 1000) for _ in range(100000)]\n",
    "\n",
    "# 将随机数写入文件\n",
    "with open('data.txt', 'w') as file:\n",
    "    for number in random_numbers:\n",
    "        file.write(str(number) + '\\n')\n",
    "\n",
    "print(\"随机数已成功写入到 data.txt 文件中！\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51dffda6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
