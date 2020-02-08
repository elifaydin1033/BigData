{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "movie=input('Write the name of a movie')\n",
    "page=int(input('Write page number'))\n",
    "data=[]\n",
    "movie=movie.replace(' ','_')\n",
    "src=False\n",
    "for x in range(1,page+1):\n",
    "    for y in range(1,6):\n",
    "        try:\n",
    "            url='https://rottentomatoes.com/m/'+movie+'/reviews?page='+str(x)\n",
    "            print(url)\n",
    "            response = requests.get(url)\n",
    "            src = response.content\n",
    "            break\n",
    "        except:\n",
    "            print ('failed attempt #',y)\n",
    "            time.sleep(2)\n",
    "    if not src:\n",
    "        print('Could not get page: ', x)\n",
    "        continue\n",
    "    else:\n",
    "        print('Successfully got page: ', x)\n",
    "    soup=BeautifulSoup(src)\n",
    "    reviews = soup.findAll('div', {'class':re.compile('row review_table_row')})\n",
    "    #print(len(reviews))\n",
    "    for review in reviews:\n",
    "        name='NA'\n",
    "        rate='NA'\n",
    "        source='NA'\n",
    "        text='NA'\n",
    "        #grab name\n",
    "        n=review.find('a', {'href':re.compile('critic')})\n",
    "        if n:\n",
    "            name=n.text\n",
    "        #grab rate\n",
    "        r=review.find('div',{'class':re.compile('review_icon icon small (.+)')}).attrs['class'][-1]\n",
    "        if r:\n",
    "            rate=r\n",
    "        #grab source\n",
    "        s=review.find('a',{'href':re.compile('source')})\n",
    "        if s:\n",
    "            source=s.find('em').text\n",
    "        #grab text\n",
    "        t=review.find('div',{'class':re.compile('the_review')})\n",
    "        if t:\n",
    "            text=t.text.strip()\n",
    "        #grab\n",
    "        d=review.find('div',{'class':re.compile('review-date')})\n",
    "        if d:\n",
    "            date=d.text.strip()\n",
    "        data.append([name,rate,source,text,date])\n",
    "    src=False   \n",
    "\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "for d in data:\n",
    "    print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('new.txt', mode='w', encoding='utf-8') as f:\n",
    "    for d in data:\n",
    "        f.write(d[0] + '\\t' + d[1] + '\\t' + d[2] + '\\t'+ d[3] + '\\t'+ d[4] +'\\n' )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Peter Bradshaw', 'fresh', 'Guardian', 'Wonderful spectacle, terrific acting and toweringly great film-making.', 'January 20, 2003']\n"
     ]
    }
   ],
   "source": [
    "with open('new.txt', mode='r', encoding = 'utf-8') as f:\n",
    "    data = f.read()\n",
    "    data = data.split('\\n')[0:-1]\n",
    "    for i in range(0,len(data)):\n",
    "        data[i] = data[i].split('\\t')\n",
    "   # print(data[50])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
