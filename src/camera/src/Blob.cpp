#include<list> 

namespace ns{
	class Blob{
		float minx;
		float miny;
		float maxx;
		float maxy;

		public: 
		    Blob(float x, float y) {
		        minx = x;
		        miny = y;
		        maxx = x;
		        maxy = y;
		    
		    }

		    void add(float x, float y) {
		        minx = std::min(minx, x);
		        miny = std::min(miny, y);
		        maxx = std::max(maxx, x);
		        maxy = std::max(maxy, y);
		    }
		    float size() {
		        return (maxx-minx)*(maxy-miny); 
		    }

		    bool isNear(float x, float y) {
				float distThreshold = 50;
		        float cx = (minx + maxx) / 2;
		        float cy = (miny + maxy) / 2;

		        float d = distSq(cx, cy, x, y);
		        if (d < distThreshold*distThreshold) {
		            return true;
		        } else {
		            return false;
		        }
		    }
		    float distSq(float x1, float y1, float x2, float y2) {
		        float d = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
		        return d;
		    }
	};
}
