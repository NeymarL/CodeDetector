/**
 * @author      LiuHe
 * @date        2016-01-28
 * @describe    k-shingles & minhashing
**/

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>
using namespace std;

void vardump(set<string>& s)
{
    for(set<string>::iterator p = s.begin(); p != s.end(); p++){
        cout << *p << endl;
    }
}

class CodeDector
{
public:
    CodeDector();
    
    CodeDector(string fileName1, string fileName2);
    
    ~CodeDector();

    bool addFile(string& filename);

    bool removeFile(int i);

    bool replaceFile(int i);

    bool readFile(string& fileName, string& file);
    
    bool k_shingles(int k, string& file, set<string>& s);

    bool compress();

    bool minhashing();

    bool generateHashFun();

private:
    int n;
    int index;
    string files[2];
    set<string> sets[2];
};


CodeDector::CodeDector(string fileName1, string fileName2)
{
    n = 2;
    readFile(fileName1, files[0]);
    readFile(fileName2, files[1]);
    // debug
    //cout << "debug" << endl;
    //cout << "file1 \n" << files[0] << endl << "file2 \n" <<  files[1] << endl;
    k_shingles(5, files[0], sets[1]);
    k_shingles(5, files[1], sets[2]);
    //vardump(sets[1]);
    //vardump(sets[2]);
}

bool addFile(string& filename)
{
    
}

/*
 * 把文件读取到内存中
 *
 * @args    string fileName :  完整文件路径 ; string file : 接收文件内容
 * @return  bool
 */
bool CodeDector::readFile(string& fileName, string& file)
{
    file.clear();
    ifstream input(fileName.c_str());
    if(input.fail()){
        cout << "Cannot open " << fileName << endl;
    }
    while(!input.eof()){
        file += input.get();
    }
    input.close();
    return true;   
}

/*
 * 分割文档中连续出现的 k 个字符构成的序列, 存储为 k-shingles 集合
 * 
 * @args    int k : 连续字符个数 ;  string fileName : 文件内容; set<string> s : 存储 k-shingles 的集合
 * @return  bool
 */
bool CodeDector::k_shingles(int k, string& file, set<string>& s)
{
    for(int i = 0; i < file.length(); i++){
        string shingle = file.substr(i, k);
        s.insert(shingle);
    }
    return true;
}

int main()
{
    cout << "test!" << endl;
    string file1 = "test1", file2 = "test2";
    CodeDector* cd = new CodeDector(file1, file2);
    return 0;
}
