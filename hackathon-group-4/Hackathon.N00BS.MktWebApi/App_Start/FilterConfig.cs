using System.Web;
using System.Web.Mvc;

namespace Hackathon.N00BS.MktWebApi
{
    public class FilterConfig
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute());
        }
    }
}
