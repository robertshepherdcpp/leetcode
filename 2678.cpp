class Solution {
public:
    int countSeniors(vector<string>& details) {
        int count = 0;
        for(auto x : details)
        {
            // auto it = std::find_if(x.begin(), x.end(), [](char a){
            //     if(int(a) >= 65 && int(a) <= 90) {return true;}
            //     else {return false;}
            // });
            // int index = 0;
            // for(int i = 0; i < x.size(); i++)
            // {
            //     if(isalpha(x[i])) {index = i;}
            // }
            //std::string str_age = x.substr(index + 1, index + 3);
            std::string str_age = x.substr(11, 2);
            if(std::stoi(str_age) > 60)
            {
                count++;
            }
        } 
        return count;    
    }
};
