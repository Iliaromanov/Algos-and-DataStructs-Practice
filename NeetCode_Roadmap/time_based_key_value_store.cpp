class TimeMap {
public:
    std::unordered_map<std::string, std::vector<std::pairjk<int, std::string>>> 
            m_timestamps_map;
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        if (const auto it = m_timestamps_map.find(key); it != m_timestamps_map.end())
            it->second.emplace_back(timestamp, value);
        else
            m_timestamps_map[key] = {std::make_pair(timestamp, value)};
    }
    
    string get(string key, int timestamp) {
        const auto it = m_timestamps_map.find(key);
        if (it == m_timestamps_map.end() || it->second.empty() || it->second[0].first > timestamp)
            return "";
        
        // do bsearch
        int l = 0, r = it->second.size() - 1;
        while (l <= r)
        {
            int m = l + (r - l) / 2;

            if (it->second[m].first == timestamp)
                return it->second[m].second;
            else if (it->second[m].first < timestamp)
                l = m + 1;
            else // it->second[m].first > timestamp
                r = m - 1;
        }

        if (l >= it->second.size())
            return it->second.back().second;

        return it->second[l-1].second;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */