from Movie import OMDBApi

if __name__ == '__main__':
    title = ''
    type = ''
    year = ''



    print('Enter a movie title to search for:')
    title = input().replace(' ', '+')
    type = 'movie'

    print('Enter the year of release or leave blank if unknown:')
    year = input()

    OMDBApi(title, type, year)
